from functools import partial
import multiprocessing
from multiprocessing.pool import ThreadPool
from selenium import webdriver
import time


def open_one_page(url):
    # 创建WebDriver对象， 相当于一个页签
    wb = webdriver.Chrome(r'D:\ProgramFiles\webdrivers\chromedriver.exe')
    # 最大等待时间为10s
    wb.implicitly_wait(10)
    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    wb.get(url)
    # 根据id查找元素，并返回一个WebElement对象
    search_area = wb.find_element_by_id("kw")
    # 操作元素，此处为输入文本到input输入框中
    search_area.send_keys('白月黑羽\n')

    # id 为 1 的元素 就是第一个搜索结果
    element = wb.find_element_by_id('1')

    # 打印出 第一个搜索结果的文本字符串
    print(element.text)
    time.sleep(10)
    wb.quit()


if __name__ == "__main__":
    # 创建WebDriver对象,相当于一个页签
    # driver = webdriver.Chrome(r'D:\ProgramFiles\webdrivers\chromedriver.exe')
    url_list = ['https://www.baidu.com']
    # 创建多线程池
    po = multiprocessing.pool.ThreadPool(5)
    # 创建多进程池
    # po = multiprocessing.Pool(5)
    po.map(partial(open_one_page), url_list)
    po.close()
    po.join()
