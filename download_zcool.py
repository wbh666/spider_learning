"""
多进程 多线程 爬取图片
"""
import os
import time
import requests
from lxml import etree
import re
from multiprocessing.pool import ThreadPool
from functools import partial
from multiprocessing import Pool


# 查找当前页面中的所有链接
def get_all_pages(index_url):
    response = requests.get(url=index_url)
    if response.status_code == 200:
        # print(response.content.decode("utf-8"))
        html = etree.HTML(response.text)
        url_list = html.xpath('//div[@class="card-box"]/div[@class="card-img"]/a/@href')
        return url_list


# 提取数据：主题，作者，图片链接
def parse_current_page(current_url):
    response = requests.get(url=current_url)
    if response.status_code == 200:
        html = etree.HTML(response.text)
        picture_group_name = html.xpath(
            '//div[@class="work-details-wrap border-bottom"]//div[@class="details-contitle-box"]/h2/text()')
        picture_group_name = [re.findall('\n                                (.*?)\n.*', i, re.S) for i in
                              picture_group_name]
        author = html.xpath('//div[@class="author-info"]//a[@class="title-content"]/text()')
        author = [re.findall('(.*?)\n.*', i, re.S) for i in author]
        picture_url_list = html.xpath(
            '//div[@class="work-center-con"]//div[@class="reveal-work-wrap '
            'text-center"]//img/@src')
        if len(picture_url_list) == 0:
            return
        print(picture_url_list)
        print(author)
        print(picture_group_name)

        dir_path = 'E:\\pictures\\' + author[0][0] + "_" + picture_group_name[0][0]
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        threadPool = ThreadPool(5)
        threadPool.map(partial(save_picture, path=dir_path), picture_url_list)
        threadPool.close()
        threadPool.join()


# 下载图片
def save_picture(picture_url, path):
    picture_name = path + os.sep + picture_url[-9:]
    with open(picture_name, 'wb+') as f:
        response = requests.get(url=picture_url)
        f.write(response.content)
        f.close()
        # time.sleep(1)


if __name__ == "__main__":
    url = "https://www.zcool.com.cn/?p=2#tab_anchor"
    po = Pool(5)
    po.map(parse_current_page, get_all_pages(url))
    po.close()
    po.join()
