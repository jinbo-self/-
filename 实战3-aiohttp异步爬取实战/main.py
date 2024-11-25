import asyncio
import json
import logging
from datetime import datetime

import aiohttp

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(levelname)s: %(message)s')

INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'

PAGE_SIZE = 18
PAGE_NUMBER = 100
CONCURRENCY = 30

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('爬取地址： %s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('爬取 %s 的时候报错了', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)


async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return await scrape_api(url)


async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    ids = []
    for index_data in results:
        if not index_data:
            continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    results = await asyncio.gather(*scrape_detail_tasks)
    logging.info('解析结果：%s', json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    now = datetime.now()
    asyncio.get_event_loop().run_until_complete(main())
    print(datetime.now() - now)
