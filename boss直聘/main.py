import json
import os
import sys
import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


def 获取Cookie():
        # 打开目标网页
    # with open('Cookies', 'r', encoding='utf-8') as file:
    #     return file.read()
        edge_options = Options()
        # edge_options.add_argument("--headless")  # 无头模式，不显示浏览器界面
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")

        # 启动 Edge 浏览器
        driver = webdriver.Edge(options=edge_options)
        try:
            # 打开目标网页
            url = "https://www.zhipin.com/web/geek/job?query=%E5%85%BB%E8%80%81%E6%8A%A4%E7%90%86%E5%91%98&city=101280100"
            driver.get(url)

            # 等待页面加载
            time.sleep(5)  # 根据网络情况调整等待时间

            # 获取 cookies
            cookies = driver.get_cookies()
            cookie_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
            print("Cookies:", cookie_str)
            return cookie_str
            # 打印 cookies
            # print("Cookies:", cookie_str)
            # with open('Cookies', 'w', encoding='utf-8') as file:
            #     file.write(cookie_str)
            # time.sleep(5)
        finally:
            # 关闭浏览器
            driver.quit()

def calculate_average(ste):
    """提取平均薪资"""
    # 提取数字部分
    parts = ste.split('-')  # 根据 '-' 分割字符串
    if len(parts) != 2:
        raise ValueError("输入格式不正确，应该是 '数字-数字K'")

    # 获取数字并转换为整数
    num1 = int(parts[0])  # 第一个数字
    num2 = num1
    match = re.search(r'-(\d+)K', ste)  # 匹配形如 '-数字K' 的模式
    if match:
        num2 = int(match.group(1))  # 返回匹配的数字部分

    # 计算平均值
    average = (num1 + num2) / 2
    return average


基本地址 = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E5%85%BB%E8%80%81%E6%8A%A4%E7%90%86%E5%91%98&city={city}&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict={multiBusinessDistrict}&multiSubway=&page={page}&pageSize={pageSize}'

cookie = '__g=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1727399482; HMACCOUNT=AB84EC718FCF1080; lastCity=101270400; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2F&s=1; __zp_seo_uuid__=32523f17-b4fe-4c6a-a9c1-58262c7b6586; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1727407950; wbg=0; __fid=522d7ea938fc77baf3c149f2f62bc91e; wt2=DTRAh-SAmhYPyimF_hgcfkzEM2HERrNDSUMoERDA19eCRf3nPXDUI-bD0bo8OQEfvomQHfyBLiybmrs-j1261aQ~~; zp_at=fEUZMVrV9lU9i8litsP7d_EenXIJEGOK4VOlc2Fe35I~; __c=1727399481; __a=56779875.1727399481..1727399481.28.1.28.28; bst=V2RNolEOD-3ltiVtRuzRUZLC-47DrQwS0~|RNolEOD-3ltiVtRuzRUZLC-47DrUwCQ~; __zp_stoken__=e468fMzbDoMK0wrbCtkEmERIPBAM9KTo2J29BMyo%2FOT0zNjU3OzM2PRk5I8OuwrjCpWHDkGHDiD80KDY1PDQzQDU5Pxg2QcSzwrk0NSzDvsK5wqdfw5Jew4kGCwRrBcKOwrcEw5TCuSnDpMK1JSYYwrY4NEE6D8K0wrTDgkLCs8K4wrtBwrbCt8K%2FNDk6NzI4Vl8GUzg5R0hTBkdbR11cSwhQT0snOkI2OcK5wovDtyw3CwwNDhIFBgMECA8QEQUJEhEQDwsJCgcIBCwzwqHCuMKMw7bDpMSdw7zEmsKaS8O0wq%2FDvMKsw7lrwplSwo5Dwq9GwqLCtlJew4BqwppDSMKmwppEwqR9WGHCvl5tdmJLw4BsZ2ZRe8OASw4NDhFfOBHDncKFw4k%3D'
Zp_token ='V2RNolEOD-3ltiVtRuzRUZLC-47DrQwS0~|RNolEOD-3ltiVtRuzRUZLC-47DrUwCQ~'
cookie = '__zp_stoken__=e468fNzrDhcK3w4LCuj0pDgsLCAhCJDc6JBg8NyY8NkA3Ojo0Qjc6QhY0J8KCwrnCk2DDjF3Dgyk5JDo6Pzk3PDo2PhQ6PsS4wrQ4OS8SwrrCml%2FDjWHDhAoPB3AIwpLCswfDl8K0JcOowroqJ8OtwrMzNzw2C8K3wrfCuz7Ct8Kzw4DDiMK5worCuDc0QEEtMwcMB1ozNENEWAlGX0NiX1IETExQJjc%2BOTbCtMKPw7MvNBIQERENCAoHBwMODA0KBgsNDAwQBAYDAwcxN8KdwrPCncOyw6zEocO%2FxJXCk1rCk0vDvMKVwr1Iwr1awq7ClcKYScKybcKOasKrwr7CqsKsYcKpwpVJwqjCgVNewr9icXldUsK8cGRpTH%2FCvFAREBINXDMMVcKnw4k%3D; __a=81308469.1727425695..1727425695.2.1.2.2; HMACCOUNT=A3539125C8ABE2F5; __c=1727425695; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1727425698; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E5%2585%25BB%25E8%2580%2581%25E6%258A%25A4%25E7%2590%2586%25E5%2591%2598%26city%3D101280100&r=&g=&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1727425698; __g=-'
cookie = '__g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1727094331; HMACCOUNT=F75F9DAC37128701; lastCity=100010000; __l=l=%2Fwww.zhipin.com%2Fc100010000-p100106%2F&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPHDLCyuiWDz86CYCXxOru1t7G1HCGM42mBVrgXcuo8IFwBZnDZWqPF64B-SAR_VxZLwSkIAjZl4GK9mR9HGyPa%26wd%3D%26eqid%3Dd1cc8c0b0081f3440000000666f15e32&g=&s=3&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1727432159; __c=1727094331; __a=69903946.1723455649.1723455649.1727094331.32.2.30.32; __zp_stoken__=e468fOj7DnMK4WsK3OSUNEg4MBEEpMz4oOzw6MkA1PTo%2BNjM7Oj4%2BFTkqwrnCtsOhw4DDjVnDh0E0JT42QDQ6ODY1PxU%2BQsS3wrk5PStIwrTDnsK6w5Fiw4kHAwNvBcKPwr8Dw5jCuSTDrMK2KSbCp8K9NzhBMwfCs8K4w4I7wrvCt8K%2Fwo3CuMKbw4E4OcOvwr97LzVYXlUQNTNSSFMHRVZHXWFREVBPUiU%2FMxU0GX%2FDtyw2EQUNDgsHCwMEBQ0JEQUEDAgQDxIDDwcICTI%2BwqDCuMKexLHDkMSdw7zEk8KUw4LCg8KiwofCnsO2R8KhXcKNwqLChG5OwqzCssK9w4BDwoPCr13CpsKTSsKtfVhcw4BTbXZbUcK5bGdnS3bDgEsPDwMRXzULIMOMw4k%3D'
Zp_token ='V2RNolEOD-3ltiVtRuzRUZLC-47DrQwS0~|RNolEOD-3ltiVtRuzRUZLC-47DrUwCQ~'



总岗位数量 = 0
总需求证书岗位 = 0
folder_path = '城市'  # 替换为您的文件夹路径
第一次读取文件 = True
已完成区域数量 = 0
for filename in os.listdir(folder_path):
    # 生成文件的完整路径
    file_path = os.path.join(folder_path, filename)
    岗位数量 = 0
    需求证书岗位 = 0
    薪资 = 0

    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)  # 读取 JSON 数据
        城市名 = data.get('zpData').get('businessDistrict').get('name')
        城市 = data.get('zpData').get('businessDistrict').get('code')
        subLevelModelList = data.get('zpData').get('businessDistrict').get('subLevelModelList')
        所有区 = []
        该城市所有区域 = {}
        # print(城市名)
        for 区 in subLevelModelList:
            当前区 = 所有区.append(区.get('code'))
            # print(区)
            if 区.get('subLevelModelList') != None:
                所有区域 = []
                for 区域 in 区.get('subLevelModelList'):
                    当前区域 = 所有区域.append(区域.get('code'))
                该城市所有区域[区.get('code')] = 所有区域
        #     print(城市名)
        #     print(城市)
        #     print(所有区)
        # print(该城市所有区域)
        # print("-----------------------------")

        for 区 in 所有区:
            for 区域 in 该城市所有区域[区]:

                for 页数 in range(1, 11):

                    with open('data.json', 'r', encoding='utf-8') as js:
                        数据 = json.load(js)  # 读取 JSON 数据
                        # print(数据)
                        if 第一次读取文件:
                            # print(城市,区,区域)
                            if 城市 == 数据.get('城市') and 区 == 数据.get('区') and 区域 == 数据.get(
                                    '区域') and 页数 == 数据.get('page'):
                                岗位数量 = 数据.get('岗位数量')
                                薪资 = 数据.get('薪资')
                                需求证书岗位 = 数据.get('需求证书岗位')
                                第一次读取文件 = False
                                pass
                            else:

                                continue
                        else:
                            pass

                    time.sleep(0.1)
                    # try:
                    headlers = {
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-encoding': 'gzip, deflate, br, zstd',
                        'Accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'Cache-control': 'no-cache',
                        'Cookie': 获取Cookie(),
                        'Pragma': 'no-cache',
                        'Priority': 'u=1, i',
                        'Referer': f'https://www.zhipin.com/web/geek/job?query=%E5%85%BB%E8%80%81%E6%8A%A4%E7%90%86%E5%91%98&city={城市}',
                        'Sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                        'Sec-ch-ua-mobile': '?0',
                        'Sec-ch-ua-platform': '"Windows"',
                        'Sec-fetch-dest': 'empty',
                        'Sec-fetch-mode': 'cors',
                        'Sec-fetch-site': 'same-origin',
                        'Token': 'ahk8YrlUNhtMnyRh',
                        'Traceid': 'F-625e03Eat4Mp6Bfd',
                        'X-requested-with': 'XMLHttpRequest',

                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.438.400 QQBrowser/13.0.6071.400',
                        'Zp_token': Zp_token
                    }
                    结果 = requests.get(
                        基本地址.format(city=城市, multiBusinessDistrict={区: 区域}, page=页数, pageSize=30),
                        headers=headlers)

                    if 结果.status_code == 200:
                        res = 结果.json()
                        print(res)
                        # print(res.get('message'))
                        if res.get('message') == '您的访问行为异常.':
                            print("行为异常")
                            保存数据 = {
                                "城市": 城市,
                                "区": 区,
                                "区域": 区域,
                                "page": 页数,
                                '薪资':薪资,
                                '需求证书岗位':需求证书岗位,
                                '岗位数量':岗位数量,
                            }
                            # 指定要保存的 JSON 文件路径
                            f = 'data.json'  # 替换为您的文件路径
                            # 使用覆盖的形式保存 JSON 文件

                            with open(f, 'w', encoding='utf-8') as jso:
                                json.dump(保存数据, jso, ensure_ascii=False, indent=4)  # 将数据写入文件
                            sys.exit("异常结束，请更新cookie")
                        jobList = res.get('zpData').get('jobList')
                        for item1 in jobList:
                            if '护理' in item1.get('jobName') and '养老' in item1.get('jobName'):
                                岗位数量 = 岗位数量 + 1
                                # print(item1.get('salaryDesc'))
                                # print(calculate_average(item1.get('salaryDesc')))
                                薪资 = 薪资 + calculate_average(item1.get('salaryDesc'))
                                for 技能需求 in item1.get('skills'):
                                    if '证' in 技能需求:
                                        需求证书岗位 = 需求证书岗位 + 1
                        print("已完成数量：", 已完成区域数量, "还剩数量：", 4610 - 已完成区域数量)
                        print("已完成任务百分比：", 已完成区域数量 / 4610)
                        # print(城市名)
                        # print("总共岗位数量:", 岗位数量)
                        # print("总薪资:", 薪资)
                        # print("平均薪资:", 薪资 / 岗位数量)
                        # print("需求证书岗位：", 需求证书岗位)
                        # print("岗位需求率：", 需求证书岗位 / 岗位数量)
                        总岗位数量 = 总岗位数量 + 岗位数量
                        # time.sleep(60)
                        print("开始保存数据------")
                        城市数据 = {
                            "城市": 城市名,
                            "总共岗位数量": 岗位数量,
                            "总薪资": 薪资,
                            "平均薪资": 薪资 / 岗位数量,
                            '需求证书岗位': 需求证书岗位,
                            '岗位需求率': 需求证书岗位 / 岗位数量,
                        }
                        # 使用覆盖的形式保存 JSON 文件
                        with open(城市名, 'w', encoding='utf-8') as jsons:
                            json.dump(城市数据, jsons, ensure_ascii=False, indent=4)  # 将数据写入文件
                            print("保存成功------")

                                # print("岗位：", item1.get('jobName'), "薪资：", item1.get('salaryDesc'), "技能要求：",
                                #       item1.get('skills'))
                    # except Exception:
                    # print(城市, "-", 区, '-', 区域, '第', 页数, '页', "没有岗位")
                    # break
                    # print(11)
                    # print(res)
                    # print(res.get('zpData'))
                    # print(res.get('zpData').get('jobList'))
                已完成区域数量 = 已完成区域数量 + 1
    with open("已完成1个城市"+城市名, 'w', encoding='utf-8') as jsons:
        json.dump("已完成1个城市"+城市名,jsons, ensure_ascii=False, indent=4)
print("总岗位数量：", 总岗位数量, '总证书岗位需求量：', 总需求证书岗位)
print("总岗位需求率：", 总需求证书岗位 / 总岗位数量)
