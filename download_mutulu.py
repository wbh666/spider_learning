import requests, os, re, time
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
from functools import partial
from multiprocessing import Pool


def save_picture(img_url, referer, path):
    file_name = path + os.sep + img_url.split('/')[-1]
    with open(file_name, 'wb+') as f:
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'Accept-Encoding': "gzip, deflate, br",
            'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'Connection': "keep-alive",
            'Cookie': 'UM_distinctid=169241b82e3d7-055c03980912f78-4c312f7f-e1000-169241b82e4370',
            'Referer': referer,
        }
        response = requests.get(img_url, headers=headers)
        f.write(response.content)
        f.close()
        time.sleep(1)


def parse_current_page(page):
    url = page[0]
    name = page[1]
    response = requests.get(url)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        img_items = soup.find('div', class_='content').find_all('img')
        img_srcs = [item['src'] for item in img_items]
        dir_path = 'E:\\picture\\' + name
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        pool = ThreadPool(4)
        pool.map(partial(save_picture, referer=url, path=dir_path), img_srcs)
        pool.close()
        pool.join()
        next_page = soup.find('div', id="pages").find_all('a')[-1]  #
        next_page = next_page['href']
        current_page_num = soup.find('div', id="pages").find('span').text
        next_page_num = re.findall('\d+', next_page)[1]
        if next_page_num != current_page_num:
            next_page = "https://www.meitulu.com" + next_page
            return parse_current_page((next_page, name))
        else:
            return


def get_all_page(index_url):
    response = requests.get(index_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')

        items = soup.find('ul', class_='img').find_all('li')
        _list = [(item.find('a')['href'], item.find_all('p')[1].text) for item in items]
        return _list


def main():
    index_url = 'https://www.meitulu.com/'
    pool = Pool(5)
    pool.map(parse_current_page, get_all_page(index_url))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
