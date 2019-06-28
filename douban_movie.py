import re
import requests
import json
import csv
import time
import matplotlib
import pandas
# -*- coding: gbk -*-
headers=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
{'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'}]
url='https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start=0'
def get_index_page(html):
    try:
        response = requests.get(url=html, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except requests.RequestException:
        print('get error')
        time.sleep(3)
        return get_index_page(html)
def parse_index_page(html):
    html = get_index_page(html)
    html = html[12:-1]
    data = json.loads(html)
    id_list = []
    if data:
        for item in data:
            id_list.append(item['url'])
    return id_list
