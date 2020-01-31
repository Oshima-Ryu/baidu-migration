import requests
import config
import datetime
import time
import json


def save_data_json(data_dict, name, time):
    file_name = str(time) + '_' + name
    with open('data/' + file_name, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, ensure_ascii=False)


def get_data(url):
    print(url)
    r = requests.get(url=url, headers=config.get_header())
    print(r.status_code)
    print(r.text)
    if r.status_code != 200:
        return False
    data_str = r.text
    start_index = data_str.find('(') + 1
    data_dict_str = data_str[start_index: data_str.__len__()-1]
    data_dict =json.loads(data_dict_str)

    return data_dict


def get_data_and_save(url, name, time):
    data = get_data(url)
    if data == False:
        return
    save_data_json(data, name, time)


def move_in_crawl():
    # move_in_province_url = 'http://huiyan.baidu.com/migration/provincerank.jsonp?dt=city&id=420100&type=move_in&date=20200130'
    # move_in_city_url = 'http://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id=420100&type=move_in&date=20200130'
    # move_in_history_url = 'http://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id=420100&type=move_in&startDate=20200101&endDate=20200130'
    pass


def move_out_crawl_daily(revert_days):
    city_name = 'wuhan'
    # 每日迁徙数据
    for i in range(revert_days):
        date = (datetime.datetime.now() + datetime.timedelta(days=-i)).strftime("%Y%m%d")
        print('##########################')
        print(i, date)
        move_out_province_url = 'http://huiyan.baidu.com/migration/provincerank.jsonp?dt=city&id=420100&type=move_out&date=%s' % date
        move_out_city_url = 'http://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id=420100&type=move_out&date=%s' % date

        get_data_and_save(move_out_province_url, city_name + '_move_out_province', date)
        time.sleep(10)
        get_data_and_save(move_out_city_url, city_name + '_move_out_city', date)
        time.sleep(10)


def move_out_crawl_month(month):
    # 月度历史迁徙数据
    # move_out_history_url = 'http://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id=420100&type=move_out&startDate=20200101&endDate=20200130'
    pass


if __name__ == '__main__':
    revert_days = 31
    move_out_crawl_daily(revert_days)
