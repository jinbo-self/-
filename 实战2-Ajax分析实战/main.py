import requests

基本地址 = 'https://spa1.scrape.center'
re = requests.get(基本地址)
页面地址 = 基本地址+'/api/movie/?limit={limit}&offset={offset}'
详情页地址 = 基本地址+'/api/movie/{id}'

def 通用爬取(url):
    # print("开始爬取数据:",url)
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.json()
        print("爬取失败")
    except requests.RequestException:
        print("解析失败")

LIMIT = 10
TOTAL_PAGE = 11
def 获取页面(page_index):
    网址 = 页面地址.format(limit=LIMIT,offset=LIMIT*(page_index-1))

    return 通用爬取(网址)

def 获取详情页(id):
    网址 = 详情页地址.format(id=id)
    return 通用爬取(网址)

def main():
    for page in range(1,TOTAL_PAGE+1):
        页面 = 获取页面(page)
        # print(页面)
        # print(页面.get('results'))
        try:
            for item in 页面.get('results'):
                id = item.get('id')
                详情页 = 获取详情页(id)
                print(详情页.get('name')+':'+详情页.get('drama'))
                print("--------------------------")
        except Exception:
            print("读取错误")

main()

