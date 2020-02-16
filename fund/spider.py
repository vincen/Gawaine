#!/usr/local/bin python3
# -*- coding: utf8 -*-

__author__ = 'vincen'

import requests
from requests.exceptions import RequestException
import json


def get_content(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_content(html):
    """返回的数据格式是：g({json})，需要去掉前后的g()，将数据解析成json"""
    # print(html)
    content = html[:-1]
    content = content[2:]
    return content


def write_to_file(content):
    with open('result-20200208.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(json.loads(content), ensure_ascii=False) + '\n')


def main():
    URL = 'http://fund.ijijin.cn/data/Net/info/all_F009_desc_0_0_1_9999_0_0_0_jsonp_g.html'
    html = get_content(URL)
    content = parse_content(html)
    write_to_file(content)


main()




