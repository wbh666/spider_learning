# 豆瓣电影top250
import requests
from lxml import etree
import pandas as pd

url = "https://movie.douban.com/top250?start={}&filter="
url_list = [url.format(i) for i in range(0, 250, 25)]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

result_list = list()
# get请求数据
for url in url_list:
    response = requests.get(url, headers=headers)
    content = etree.HTML(response.content.decode('utf-8'))
    name = content.xpath('//div[@class="item"]//span[@class="title"][1]/text()')
    rating_num = content.xpath('//div[@class="item"]//span[@class="rating_num"]/text()')
    for i in range(len(name)):
        result = name[i]+" "+rating_num[i]+" "
        result_list.append(result)


stream = pd.Series(result_list)
stream.to_csv("豆瓣电影top250.csv", header=False)
