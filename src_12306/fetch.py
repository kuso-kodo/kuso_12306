import datetime
import json
import pickle
import re
import time
import warnings

import requests

UA = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  + 'AppleWebKit/537.36 (KHTML, like Gecko) '
                  + 'Chrome/73.0.3683.86 Safari/537.36'}


class Ticket:
    def __init__(self, result_list):
        self.train_number = result_list[2]
        self.train_name = result_list[3]
        self.train_start = result_list[4]
        self.train_end = result_list[5]
        self.ticket_from = result_list[6]
        self.ticket_to = result_list[7]
        self.ticket_start_time = result_list[8]
        self.ticket_end_time = result_list[9]
        self.ticket_length = result_list[10]
        self.ticket_date = result_list[13]
        self.ticket_from_station_number = result_list[16]
        self.ticket_to_station_number = result_list[17]
        self.seat_types = result_list[35]
        self.price = "-1"
        if self.seat_types != '':
            self.get_ticket_price()

    def get_ticket_price(self):
        fake_query_url = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPriceFL?train_no='
        query_url = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no='
        param = self.train_number \
                + '&from_station_no=' \
                + self.ticket_from_station_number \
                + '&to_station_no=' + self.ticket_to_station_number \
                + '&seat_types=' \
                + self.seat_types \
                + '&train_date=' \
                + self.ticket_date[0:4] + '-' \
                + self.ticket_date[4:6] + '-' \
                + self.ticket_date[6:8]
        try:
            requests.get(fake_query_url + param, verify=False, headers=UA)
        except Exception:
            pass
        response = requests.get(query_url + param, headers=UA)
        if response.content:
            data = response.json()['data']
            try:
                # 二等座
                self.price = data['O'].strip('¥')
            except Exception:
                try:
                    # 硬卧二等
                    self.price = data['A3'].strip('¥')
                except Exception:
                    try:
                        # 无座
                        self.price = data['WZ'].strip('¥')
                    except Exception:
                        self.price = "-1"  # error
        else:
            self.price = "-1"


def get_all_stations():
    response = requests.get(queryGetStation, verify=False, headers=UA)
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    return dict(stations)


queryGetStation = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9042'
stations = get_all_stations()


def generate_query_url(from_city, to_city):
    fromStation = stations[from_city]
    toStation = stations[to_city]
    date = datetime.datetime.now() + datetime.timedelta(days=7)
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=' + date.date().isoformat() + '&leftTicketDTO.from_station=' + fromStation + '&leftTicketDTO.to_station=' + toStation + '&purpose_codes=ADULT'
    return url


if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    city_list = ['北京', '天津', '上海', '重庆', '石家庄',
                 '太原', '呼和浩特', '郑州', '长沙', '武汉',
                 '哈尔滨', '长春', '沈阳', '成都', '昆明',
                 '贵阳', '拉萨', '乌鲁木齐', '西安', '兰州',
                 '银川', '西宁', '广州', '南宁', '海口',
                 '南京', '杭州', '福州', '济南', '南昌',
                 '合肥']

    try:
        with open('fetched.tmp', 'rb') as f:
            fetched = pickle.load(f)
        with open('final.tmp', 'rb') as f:
            final = pickle.load(f)
    except Exception:
        fetched = []
        final = []
    for i in city_list:
        for j in city_list:
            if i != j and i + j not in fetched:
                print("Fetching: " + i + " to " + j)
                fetched.append(i + j)
                r = requests.get(generate_query_url(i, j), verify=False, headers=UA)
                result = r.json()['data']['result']
                if result:
                    listo = []
                    for item in result:
                        listo.append(Ticket(item.split('|')))
                        time.sleep(0.2)
                    final.extend([obj.__dict__ for obj in listo if obj.price != "-1"])
            time.sleep(0.5)
            with open('fetched.tmp', 'wb') as f:
                pickle.dump(fetched, f)
            with open('final.tmp', 'wb') as f:
                pickle.dump(final, f)

    with open('test.json', 'w') as out:
        json.dump(final, out)
