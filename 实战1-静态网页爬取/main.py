import logging
import multiprocessing
import re
from urllib.parse import urljoin

import requests

from 保存数据 import save_Data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:%(message)s')
BASE_URL = "https://ssr1.scrape.center"
TOTAL_PAGE = 10


def scrape_page(url):
    """获取列表页面"""
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.info('valid status code %s while scraping %s',
                     response.status_code, url)
    except requests.RequestException:
        # exc_info 打印堆栈
        logging.info('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    """根据索引获取页面"""
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    """解析获取的当前界面。返回详情列表指"""
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', detail_url)
        yield detail_url  # 返回一个生成器，该生成器可以迭代，也可以定义一个列表返回


def scrape_detail(url):
    return scrape_page(url)


def parse_detail(html):
    封面_匹配模式 = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    名字_匹配模式 = re.compile('class="item.*?<h2.*?class="m-b-sm">(.*?)</h2>', re.S)

    封面 = re.search(封面_匹配模式, html).group(1).strip() if re.search(封面_匹配模式, html) else None

    名字 = re.search(名字_匹配模式, html).group(1).strip() if re.search(名字_匹配模式, html) else None

    return {'封面': 封面,
            '名字': 名字}


def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    # logging.info('detail urls %s', detail_urls)
    for detail_url in detail_urls:
        # 调用生成器，遍历的同时也会打印每次遍历的日志，日志也会在生成器里
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail  %s', data)
        logging.info("存储")
        save_Data(data)


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1,TOTAL_PAGE+1)
    pool.map(main,pages)
    pool.close()
    pool.join()
