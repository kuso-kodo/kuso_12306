# -*- coding: utf-8 -*-
# Ctrip Sucks!

import json
import pickle

import eventlet

requests = eventlet.import_patched('requests')

# Auto generated
cities = {
    '北京': {
        'cityid': '1',
        'code': 'BJS'
    },
    '西安': {
        'cityid': '10',
        'code': 'SIA'
    },
    '咸阳': {
        'cityid': '10',
        'code': 'SIA'
    },
    '兰州': {
        'cityid': '100',
        'code': 'LHW'
    },
    '呼和浩特': {
        'cityid': '103',
        'code': 'HET'
    },
    '太原': {
        'cityid': '105',
        'code': 'TYN'
    },
    '林芝': {
        'cityid': '108',
        'code': 'LZY'
    },
    '满洲里': {
        'cityid': '1083',
        'code': 'NZH'
    },
    '攀枝花': {
        'cityid': '1097',
        'code': 'PZI'
    },
    '敦煌': {
        'cityid': '11',
        'code': 'DNH'
    },
    '延安': {
        'cityid': '110',
        'code': 'ENY'
    },
    '日照': {
        'cityid': '1106',
        'code': 'RIZ'
    },
    '邵阳': {
        'cityid': '1111',
        'code': 'WGN'
    },
    '白城': {
        'cityid': '1116',
        'code': 'DBC'
    },
    '荆门': {
        'cityid': '1121',
        'code': 'JM1'
    },
    '乌海': {
        'cityid': '1133',
        'code': 'WUA'
    },
    '扎兰屯': {
        'cityid': '1135',
        'code': 'NZL'
    },
    '兴义': {
        'cityid': '1139',
        'code': 'ACX'
    },
    '百色': {
        'cityid': '1140',
        'code': 'AEB'
    },
    '加格达奇': {
        'cityid': '1143',
        'code': 'JGD'
    },
    '金昌': {
        'cityid': '1158',
        'code': 'JIC'
    },
    '宁蒗': {
        'cityid': '1161',
        'code': 'NLH'
    },
    '南京': {
        'cityid': '12',
        'code': 'NKG'
    },
    '盐城': {
        'cityid': '1200',
        'code': 'YNZ'
    },
    '稻城': {
        'cityid': '1222',
        'code': 'DCY'
    },
    '铜仁': {
        'cityid': '1227',
        'code': 'TEN'
    },
    '临沧': {
        'cityid': '1236',
        'code': 'LNJ'
    },
    '西宁': {
        'cityid': '124',
        'code': 'XNN'
    },
    '汉中': {
        'cityid': '129',
        'code': 'HZG'
    },
    '无锡': {
        'cityid': '13',
        'code': 'WUX'
    },
    '营口': {
        'cityid': '1300',
        'code': 'YKH'
    },
    '松原': {
        'cityid': '1303',
        'code': 'YSQ'
    },
    '格尔木': {
        'cityid': '132',
        'code': 'GOQ'
    },
    '大同': {
        'cityid': '136',
        'code': 'DAT'
    },
    '长治': {
        'cityid': '137',
        'code': 'CIH'
    },
    '临汾': {
        'cityid': '139',
        'code': 'LFQ'
    },
    '运城': {
        'cityid': '140',
        'code': 'YCU'
    },
    '包头': {
        'cityid': '141',
        'code': 'BAV'
    },
    '海拉尔': {
        'cityid': '142',
        'code': 'HLD'
    },
    '济南': {
        'cityid': '144',
        'code': 'TNA'
    },
    '秦皇岛': {
        'cityid': '147',
        'code': 'BPE'
    },
    '齐齐哈尔': {
        'cityid': '149',
        'code': 'NDG'
    },
    '扬州': {
        'cityid': '15',
        'code': 'YTY'
    },
    '牡丹江': {
        'cityid': '150',
        'code': 'MDG'
    },
    '漠河': {
        'cityid': '155',
        'code': 'OHE'
    },
    '鸡西': {
        'cityid': '157',
        'code': 'JXA'
    },
    '长春': {
        'cityid': '158',
        'code': 'CGQ'
    },
    '建三江': {
        'cityid': '1623',
        'code': 'JSJ'
    },
    '阿尔山': {
        'cityid': '1658',
        'code': 'YIE'
    },
    '克拉玛依': {
        'cityid': '166',
        'code': 'KRY'
    },
    '杭州': {
        'cityid': '17',
        'code': 'HGH'
    },
    '荔波': {
        'cityid': '1708',
        'code': 'LLB'
    },
    '阿克苏': {
        'cityid': '173',
        'code': 'AKU'
    },
    '阿勒泰': {
        'cityid': '175',
        'code': 'AAT'
    },
    '安庆': {
        'cityid': '177',
        'code': 'AQG'
    },
    '鞍山': {
        'cityid': '178',
        'code': 'AOG'
    },
    '安顺': {
        'cityid': '179',
        'code': 'AVA'
    },
    '腾冲': {
        'cityid': '1819',
        'code': 'TCZ'
    },
    '北海': {
        'cityid': '189',
        'code': 'BHY'
    },
    '舟山': {
        'cityid': '19',
        'code': 'HSN'
    },
    '保山': {
        'cityid': '197',
        'code': 'BSD'
    },
    '白山': {
        'cityid': '199',
        'code': 'NBS'
    },
    '上海': {
        'cityid': '2',
        'code': 'SHA'
    },
    '常德': {
        'cityid': '201',
        'code': 'CGD'
    },
    '赤峰': {
        'cityid': '202',
        'code': 'CIF'
    },
    '长沙': {
        'cityid': '206',
        'code': 'CSX'
    },
    '祁连': {
        'cityid': '20892',
        'code': 'HBQ'
    },
    '文山': {
        'cityid': '20963',
        'code': 'WNH'
    },
    '霍林郭勒': {
        'cityid': '21091',
        'code': 'HUO'
    },
    '朝阳': {
        'cityid': '211',
        'code': 'CHG'
    },
    '玉树': {
        'cityid': '21114',
        'code': 'YUS'
    },
    '乌拉特中旗': {
        'cityid': '21184',
        'code': 'WZQ'
    },
    '阿拉善左旗': {
        'cityid': '21269',
        'code': 'AXF'
    },
    '常州': {
        'cityid': '213',
        'code': 'CZX'
    },
    '额济纳旗': {
        'cityid': '21339',
        'code': 'EJN'
    },
    '喀什': {
        'cityid': '21358',
        'code': 'KHG'
    },
    '哈密': {
        'cityid': '21395',
        'code': 'HMI'
    },
    '潮州': {
        'cityid': '215',
        'code': 'SWA'
    },
    '澜沧': {
        'cityid': '21596',
        'code': 'JMJ'
    },
    '若羌': {
        'cityid': '21737',
        'code': 'RQA'
    },
    '沧源': {
        'cityid': '21741',
        'code': 'CWJ'
    },
    '池州': {
        'cityid': '218',
        'code': 'JUH'
    },
    '吐鲁番': {
        'cityid': '21811',
        'code': 'TLQ'
    },
    '莎车': {
        'cityid': '21827',
        'code': 'QSZ'
    },
    '果洛': {
        'cityid': '21862',
        'code': 'GMQ'
    },
    '阿拉善右旗': {
        'cityid': '21863',
        'code': 'RHT'
    },
    '抚远': {
        'cityid': '21943',
        'code': 'FYJ'
    },
    '毕节': {
        'cityid': '22031',
        'code': 'BFJ'
    },
    '丹东': {
        'cityid': '221',
        'code': 'DDG'
    },
    '黄山': {
        'cityid': '23',
        'code': 'TXN'
    },
    '大庆': {
        'cityid': '231',
        'code': 'DQA'
    },
    '达县': {
        'cityid': '234',
        'code': 'DAX'
    },
    '达州': {
        'cityid': '234',
        'code': 'DAX'
    },
    '东营': {
        'cityid': '236',
        'code': 'DOY'
    },
    '九江': {
        'cityid': '24',
        'code': 'JIU'
    },
    '恩施': {
        'cityid': '245',
        'code': 'ENH'
    },
    '厦门': {
        'cityid': '25',
        'code': 'XMN'
    },
    '德令哈': {
        'cityid': '2542',
        'code': 'HXD'
    },
    '博乐': {
        'cityid': '2548',
        'code': 'BPL'
    },
    '富蕴': {
        'cityid': '255',
        'code': 'FYN'
    },
    '阜阳': {
        'cityid': '257',
        'code': 'FUG'
    },
    '福州': {
        'cityid': '258',
        'code': 'FOC'
    },
    '武夷山': {
        'cityid': '26',
        'code': 'WUS'
    },
    '广元': {
        'cityid': '267',
        'code': 'GYS'
    },
    '赣州': {
        'cityid': '268',
        'code': 'KOW'
    },
    '张家界': {
        'cityid': '27',
        'code': 'DYG'
    },
    '邯郸': {
        'cityid': '275',
        'code': 'HDG'
    },
    '合肥': {
        'cityid': '278',
        'code': 'HFE'
    },
    '成都': {
        'cityid': '28',
        'code': 'CTU'
    },
    '黑河': {
        'cityid': '281',
        'code': 'HEK'
    },
    '怀化': {
        'cityid': '282',
        'code': 'HJJ'
    },
    '和田': {
        'cityid': '294',
        'code': 'HTN'
    },
    '衡阳': {
        'cityid': '297',
        'code': 'HNY'
    },
    '惠阳': {
        'cityid': '298',
        'code': 'HUZ'
    },
    '惠州': {
        'cityid': '299',
        'code': 'HUZ'
    },
    '天津': {
        'cityid': '3',
        'code': 'TSN'
    },
    '深圳': {
        'cityid': '30',
        'code': 'SZX'
    },
    '景德镇': {
        'cityid': '305',
        'code': 'JDZ'
    },
    '梅县': {
        'cityid': '3053',
        'code': 'MXZ'
    },
    '梅州': {
        'cityid': '3053',
        'code': 'MXZ'
    },
    '井冈山': {
        'cityid': '307',
        'code': 'JGS'
    },
    '景洪': {
        'cityid': '309',
        'code': 'JHG'
    },
    '珠海': {
        'cityid': '31',
        'code': 'ZUH'
    },
    '佳木斯': {
        'cityid': '317',
        'code': 'JMU'
    },
    '济宁': {
        'cityid': '318',
        'code': 'JNG'
    },
    '广州': {
        'cityid': '32',
        'code': 'CAN'
    },
    '固原': {
        'cityid': '321',
        'code': 'GYU'
    },
    '芷江': {
        'cityid': '3229',
        'code': 'HJJ'
    },
    '嘉峪关': {
        'cityid': '326',
        'code': 'JGN'
    },
    '锦州': {
        'cityid': '327',
        'code': 'JNZ'
    },
    '库车': {
        'cityid': '329',
        'code': 'KCA'
    },
    '桂林': {
        'cityid': '33',
        'code': 'KWL'
    },
    '库尔勒': {
        'cityid': '330',
        'code': 'KRL'
    },
    '布尔津': {
        'cityid': '3326',
        'code': 'KJI'
    },
    '凯里': {
        'cityid': '333',
        'code': 'KJH'
    },
    '新源': {
        'cityid': '3360',
        'code': 'NLT'
    },
    '昆明': {
        'cityid': '34',
        'code': 'KMG'
    },
    '连城': {
        'cityid': '348',
        'code': 'LCX'
    },
    '龙岩': {
        'cityid': '348',
        'code': 'LCX'
    },
    '西双版纳': {
        'cityid': '35',
        'code': 'JHG'
    },
    '洛阳': {
        'cityid': '350',
        'code': 'LYA'
    },
    '连云港': {
        'cityid': '353',
        'code': 'LYG'
    },
    '柳州': {
        'cityid': '354',
        'code': 'LZH'
    },
    '泸州': {
        'cityid': '355',
        'code': 'LZO'
    },
    '大理': {
        'cityid': '36',
        'code': 'DLU'
    },
    '丽江': {
        'cityid': '37',
        'code': 'LJG'
    },
    '绵阳': {
        'cityid': '370',
        'code': 'MIG'
    },
    '宁波': {
        'cityid': '375',
        'code': 'NGB'
    },
    '南昌': {
        'cityid': '376',
        'code': 'KHN'
    },
    '南充': {
        'cityid': '377',
        'code': 'NAO'
    },
    '贵阳': {
        'cityid': '38',
        'code': 'KWE'
    },
    '南宁': {
        'cityid': '380',
        'code': 'NNG'
    },
    '台南': {
        'cityid': '3847',
        'code': 'TNN'
    },
    '台东': {
        'cityid': '3848',
        'code': 'TTT'
    },
    '台中': {
        'cityid': '3849',
        'code': 'RMQ'
    },
    '南阳': {
        'cityid': '385',
        'code': 'NNY'
    },
    '黎平': {
        'cityid': '3852',
        'code': 'HZH'
    },
    '巴彦淖尔': {
        'cityid': '3887',
        'code': 'RLK'
    },
    '乌鲁木齐': {
        'cityid': '39',
        'code': 'URC'
    },
    '河池': {
        'cityid': '3969',
        'code': 'HCJ'
    },
    '鄂尔多斯': {
        'cityid': '3976',
        'code': 'DSN'
    },
    '且末': {
        'cityid': '399',
        'code': 'IQM'
    },
    '普洱': {
        'cityid': '3996',
        'code': 'SYM'
    },
    '德宏': {
        'cityid': '3997',
        'code': 'LUM'
    },
    '芒市': {
        'cityid': '3997',
        'code': 'LUM'
    },
    '重庆': {
        'cityid': '4',
        'code': 'CKG'
    },
    '庆阳': {
        'cityid': '404',
        'code': 'IQN'
    },
    '晋江': {
        'cityid': '406',
        'code': 'JJN'
    },
    '泉州': {
        'cityid': '406',
        'code': 'JJN'
    },
    '石狮': {
        'cityid': '406',
        'code': 'JJN'
    },
    '衢州': {
        'cityid': '407',
        'code': 'JUZ'
    },
    '拉萨': {
        'cityid': '41',
        'code': 'LXA'
    },
    '上饶': {
        'cityid': '411',
        'code': 'SQD'
    },
    '康定': {
        'cityid': '4130',
        'code': 'KGT'
    },
    '海口': {
        'cityid': '42',
        'code': 'HAK'
    },
    '呼伦贝尔': {
        'cityid': '4255',
        'code': 'XRQ'
    },
    '石河子': {
        'cityid': '426',
        'code': 'SHF'
    },
    '石家庄': {
        'cityid': '428',
        'code': 'SJW'
    },
    '三亚': {
        'cityid': '43',
        'code': 'SYX'
    },
    '三明': {
        'cityid': '437',
        'code': 'SQJ'
    },
    '汕头': {
        'cityid': '447',
        'code': 'SWA'
    },
    '沈阳': {
        'cityid': '451',
        'code': 'SHE'
    },
    '十堰': {
        'cityid': '452',
        'code': 'WDS'
    },
    '塔城': {
        'cityid': '455',
        'code': 'TCG'
    },
    '通化': {
        'cityid': '456',
        'code': 'TNH'
    },
    '通辽': {
        'cityid': '458',
        'code': 'TGO'
    },
    '天水': {
        'cityid': '464',
        'code': 'THQ'
    },
    '唐山': {
        'cityid': '468',
        'code': 'TVS'
    },
    '五大连池': {
        'cityid': '473',
        'code': 'DTU'
    },
    '潍坊': {
        'cityid': '475',
        'code': 'WEF'
    },
    '武汉': {
        'cityid': '477',
        'code': 'WUH'
    },
    '威海': {
        'cityid': '479',
        'code': 'WEH'
    },
    '乌兰浩特': {
        'cityid': '484',
        'code': 'HLH'
    },
    '万州': {
        'cityid': '487',
        'code': 'WXN'
    },
    '温州': {
        'cityid': '491',
        'code': 'WNZ'
    },
    '梧州': {
        'cityid': '492',
        'code': 'WUZ'
    },
    '西昌': {
        'cityid': '494',
        'code': 'XIC'
    },
    '襄阳': {
        'cityid': '496',
        'code': 'XFN'
    },
    '夏河': {
        'cityid': '497',
        'code': 'GXH'
    },
    '哈尔滨': {
        'cityid': '5',
        'code': 'HRB'
    },
    '锡林浩特': {
        'cityid': '500',
        'code': 'XIL'
    },
    '信阳': {
        'cityid': '510',
        'code': 'XAI'
    },
    '徐州': {
        'cityid': '512',
        'code': 'XUZ'
    },
    '忻州': {
        'cityid': '513',
        'code': 'WUT'
    },
    '宜宾': {
        'cityid': '514',
        'code': 'YBP'
    },
    '宜昌': {
        'cityid': '515',
        'code': 'YIH'
    },
    '嘉义': {
        'cityid': '5152',
        'code': 'CYI'
    },
    '伊春': {
        'cityid': '517',
        'code': 'LDS'
    },
    '宜春': {
        'cityid': '518',
        'code': 'YIC'
    },
    '琼海': {
        'cityid': '52',
        'code': 'BAR'
    },
    '延吉': {
        'cityid': '523',
        'code': 'YNJ'
    },
    '榆林': {
        'cityid': '527',
        'code': 'UYN'
    },
    '伊犁': {
        'cityid': '529',
        'code': 'YIN'
    },
    '伊宁': {
        'cityid': '529',
        'code': 'YIN'
    },
    '烟台': {
        'cityid': '533',
        'code': 'YNT'
    },
    '义乌': {
        'cityid': '536',
        'code': 'YIW'
    },
    '马公': {
        'cityid': '5383',
        'code': 'MZG'
    },
    '澎湖列岛': {
        'cityid': '5383',
        'code': 'MZG'
    },
    '湛江': {
        'cityid': '547',
        'code': 'ZHA'
    },
    '张家口': {
        'cityid': '550',
        'code': 'ZQZ'
    },
    '昭通': {
        'cityid': '555',
        'code': 'ZAT'
    },
    '中卫': {
        'cityid': '556',
        'code': 'ZHY'
    },
    '遵义': {
        'cityid': '558',
        'code': 'ZYI'
    },
    '郑州': {
        'cityid': '559',
        'code': 'CGO'
    },
    '承德': {
        'cityid': '562',
        'code': 'CDE'
    },
    '临沂': {
        'cityid': '569',
        'code': 'LYI'
    },
    '昌都': {
        'cityid': '575',
        'code': 'BPX'
    },
    '淮安': {
        'cityid': '577',
        'code': 'HIA'
    },
    '台州': {
        'cityid': '578',
        'code': 'HYN'
    },
    '泰州': {
        'cityid': '579',
        'code': 'YTY'
    },
    '香港': {
        'cityid': '58',
        'code': 'HKG'
    },
    '澳门': {
        'cityid': '59',
        'code': 'MFM'
    },
    '大连': {
        'cityid': '6',
        'code': 'DLC'
    },
    '六盘水': {
        'cityid': '605',
        'code': 'LPF'
    },
    '台北': {
        'cityid': '617',
        'code': 'TPE'
    },
    '神农架': {
        'cityid': '657',
        'code': 'HPG'
    },
    '张掖': {
        'cityid': '663',
        'code': 'YZY'
    },
    '遵义茅台': {
        'cityid': '669329',
        'code': 'WMT'
    },
    '花莲': {
        'cityid': '6954',
        'code': 'HUN'
    },
    '青岛': {
        'cityid': '7',
        'code': 'TAO'
    },
    '高雄': {
        'cityid': '720',
        'code': 'KHH'
    },
    '金门': {
        'cityid': '7203',
        'code': 'KNH'
    },
    '乌兰察布': {
        'cityid': '7518',
        'code': 'UCB'
    },
    '二连浩特': {
        'cityid': '7626',
        'code': 'ERL'
    },
    '吕梁': {
        'cityid': '7631',
        'code': 'LLV'
    },
    '陇南': {
        'cityid': '7707',
        'code': 'LNL'
    },
    '黔江': {
        'cityid': '7708',
        'code': 'JIQ'
    },
    '马祖': {
        'cityid': '7808',
        'code': 'MFK'
    },
    '红原': {
        'cityid': '7835',
        'code': 'AHJ'
    },
    '南通': {
        'cityid': '82',
        'code': 'NTG'
    },
    '花土沟': {
        'cityid': '83679',
        'code': 'HTT'
    },
    '九寨沟': {
        'cityid': '91',
        'code': 'JZH'
    },
    '南竿': {
        'cityid': '91804',
        'code': 'LZN'
    },
    '日喀则': {
        'cityid': '92',
        'code': 'RKZ'
    },
    '迪庆': {
        'cityid': '93',
        'code': 'DIG'
    },
    '香格里拉': {
        'cityid': '93',
        'code': 'DIG'
    },
    '潮汕': {
        'cityid': '956',
        'code': 'SWA'
    },
    '揭阳': {
        'cityid': '956',
        'code': 'SWA'
    },
    '阿里': {
        'cityid': '97',
        'code': 'NGQ'
    },
    '永州': {
        'cityid': '970',
        'code': 'LLF'
    },
    '银川': {
        'cityid': '99',
        'code': 'INC'
    }
}


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def get_resp(url, data, header):
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.post(url, data=data, headers=header, proxies={"http": "http://{}".format(proxy)})
            return html
        except Exception:
            retry_count -= 1
    delete_proxy(proxy)
    return None


def get_flight_prices(site_info, time_info):
    url = 'https://flights.ctrip.com/itinerary/api/12808/products'
    headers = {'referer': 'https://flights.ctrip.com/itinerary/oneway',
               'content-type': 'application/json'}
    data = {
        "flightWay": "Oneway",
        "classType": "ALL",
        "hasChild": False,
        "hasBaby": False,
        "searchIndex": 1,
        "airportParams": [{
            "dcity": site_info['depart']['city'],
            "acity": site_info['arrive']['city'],
            "dcityname": site_info['depart']['cityname'],
            "acityname": site_info['arrive']['cityname'],
            "date": time_info['date'],
            "dcityid": site_info['depart']['cityid'],
            "acityid": site_info['arrive']['cityid']
        }]
    }
    res = None
    while not res:
        res = get_resp(url, json.dumps(data), headers)
    if 200 <= res.status_code < 300:
        return parse(res.text)
    else:
        print('CTrip Sucks')
        return []


def parse(res):
    if not res:
        return []
    prices = []
    try:
        jdata = json.loads(res)
    except json.JSONDecodeError:
        return prices
    for route in jdata.get('data', {}).get('routeList') or []:
        if not route:
            continue
        for leg in route['legs']:
            if leg.get('characteristic') and \
                    leg['characteristic'].get('lowestPrice'):
                prices.append({
                    'price': leg['characteristic']['lowestPrice'],
                    'depart_time': leg['flight']['departureDate'],
                    'arrival_time': leg['flight']['arrivalDate'],
                    'number': leg['flight']['flightNumber'],
                    'from': leg['flight']['departureAirportInfo']['cityName'],
                    'to': leg['flight']['arrivalAirportInfo']['cityName'],
                })
    return prices


def get_list(from_city, to_city):
    leave_day = '2019-04-22'

    leave_time_start = leave_day + " 00:00:00"
    leave_time_end = leave_day + " 23:59:00"

    depart = {'city': cities[from_city]['code'], 'cityname': from_city, 'cityid': cities[from_city]['cityid']}
    arrive = {'city': cities[to_city]['code'], 'cityname': to_city, 'cityid': cities[to_city]['cityid']}
    site_info = {'depart': depart, 'arrive': arrive}
    time_info = {
        'date': leave_day,
        'before': leave_time_end,
        'after': leave_time_start,
        'train_minutes': 940}
    return get_flight_prices(site_info, time_info)


def main():
    city_list = ['北京', '上海', '天津', '重庆', '哈尔滨', '长春', '沈阳', '呼和浩特', '石家庄', '乌鲁木齐', '兰州', '西宁', '西安', '银川', '郑州', '济南',
                 '太原', '合肥', '武汉', '南京', '成都', '贵阳', '昆明', '南宁', '杭州', '南昌', '广州', '福州', '海口']
    try:
        with open('ffetched.tmp', 'rb') as f:
            fetched = pickle.load(f)
        with open('ffinal.tmp', 'rb') as f:
            final = pickle.load(f)
    except Exception:
        fetched = []
        final = []
    for i in city_list:
        for j in city_list:
            if i != j and i + j not in fetched:
                final.extend(get_list(i, j))
                fetched.append(i + j)

    with open('ftest.json', 'w') as out:
        json.dump(final, out)


if __name__ == "__main__":
    success = False
    while not success:
        try:
            main()
            success = True
        except Exception:
            print('Fuck')
