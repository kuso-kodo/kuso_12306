import json
import pickle

import src_12306.fetch

if __name__ == '__main__':
    # dump stations file
    stations = src_12306.fetch.stations
    with open('stations.json', 'w', encoding='utf-8') as fout:
        json.dump(stations, fout, indent=2, sort_keys=True, ensure_ascii=False)

    with open('final.tmp', 'rb') as f:
        final = pickle.load(f)

    for items in final:
        del items['seat_types']
        del items['ticket_date']
        del items['ticket_from_station_number']
        del items['ticket_to_station_number']
        del items['train_start']
        del items['train_end']
        del items['train_number']
        items['price'] = float(items['price'])

    with open('output.json', 'w') as fout:
        json.dump(final, fout, indent=2, sort_keys=True)
