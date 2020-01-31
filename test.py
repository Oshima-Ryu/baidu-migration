import datetime
import requests
import config
import json
import os


def data_test():
    now_day = datetime.datetime.now().strftime("%Y%m%d")
    revert_days = 31
    for i in range(revert_days):
        print(i, (datetime.datetime.now() + datetime.timedelta(days=-i)).strftime("%Y%m%d"))


def extract_data_test():
    move_in_province_url = 'http://huiyan.baidu.com/migration/provincerank.jsonp?dt=city&id=420100&type=move_in&date=20200130'
    move_in_province_url = 'http://huiyan.baidu.com/migration/provincerank.jsonp?dt=city&id=420100&type=move_out&date=20200131'
    r = requests.get(url=move_in_province_url, headers=config.get_header())
    print(r.status_code)
    print(r.text)

    # str = 'cb({"errno":0,"errmsg":"SUCCESS","data":{"list":[{"province_name":"\u6e56\u5317\u7701","value":82.55},{"province_name":"\u6e56\u5357\u7701","value":2.58},{"province_name":"\u6cb3\u5357\u7701","value":2.21},{"province_name":"\u5e7f\u4e1c\u7701","value":2},{"province_name":"\u6c5f\u897f\u7701","value":0.93},{"province_name":"\u5b89\u5fbd\u7701","value":0.92},{"province_name":"\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a","value":0.89},{"province_name":"\u91cd\u5e86\u5e02","value":0.85},{"province_name":"\u56db\u5ddd\u7701","value":0.77},{"province_name":"\u6c5f\u82cf\u7701","value":0.73},{"province_name":"\u798f\u5efa\u7701","value":0.59},{"province_name":"\u4e91\u5357\u7701","value":0.58},{"province_name":"\u5c71\u4e1c\u7701","value":0.57},{"province_name":"\u6cb3\u5317\u7701","value":0.55},{"province_name":"\u6d77\u5357\u7701","value":0.51},{"province_name":"\u5317\u4eac\u5e02","value":0.46},{"province_name":"\u4e0a\u6d77\u5e02","value":0.32},{"province_name":"\u8d35\u5dde\u7701","value":0.28},{"province_name":"\u9655\u897f\u7701","value":0.27},{"province_name":"\u6d59\u6c5f\u7701","value":0.24},{"province_name":"\u5c71\u897f\u7701","value":0.13},{"province_name":"\u5929\u6d25\u5e02","value":0.12},{"province_name":"\u9ed1\u9f99\u6c5f\u7701","value":0.11},{"province_name":"\u5409\u6797\u7701","value":0.1},{"province_name":"\u7518\u8083\u7701","value":0.1},{"province_name":"\u8fbd\u5b81\u7701","value":0.08},{"province_name":"\u9752\u6d77\u7701","value":0.07},{"province_name":"\u5185\u8499\u53e4\u81ea\u6cbb\u533a","value":0.07},{"province_name":"\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a","value":0.04},{"province_name":"\u897f\u85cf\u81ea\u6cbb\u533a","value":0.03},{"province_name":"\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a","value":0.03}]}})'
    #
    # start_index = str.find('(')
    # print(start_index)
    # str = str[start_index+1: str.__len__()-1]
    # print(type(str))
    # data_json = json.loads(str)
    #
    # item = json.dumps(data_json)
    #
    #
    # with open('data/data2.json', 'w', encoding='utf-8') as f:
    #     json.dump(data_json, f, ensure_ascii=False)


if __name__ == '__main__':
    extract_data_test()
    # data_test()
