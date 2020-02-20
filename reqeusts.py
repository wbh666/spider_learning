import requests
from lxml import etree
url = "https://tieba.baidu.com/f?kw=dota2&ie=utf-8&cid=&tab=corearea&pn=100"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
response = requests.get(url=url)

html = etree.HTML(response.text)

name = html.xpath('//li[@class=" j_thread_list clearfix"]//a[@class="j_th_tit "]/text()')
author = html.xpath('//li[@class=" j_thread_list clearfix"]//span/@title')
print(name)
