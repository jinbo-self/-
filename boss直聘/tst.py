# #
# # from selenium import webdriver
# # import time
# # import json
# # def 获取cookie(url,cookie文件名):
# #     #1. 打开浏览器
# #     driver = webdriver.Edge()
# #     #2. 进入网页
# #     driver.get(url)
# #     #3. 进入网页之后，手动点击登录页码快速登录进去
# #     time.sleep(15)
# #     #4.在15s之内登录，获取所有cookie信息(返回是字典)
# #     dictCookies = driver.get_cookies()
# #     for cookie in dictCookies:
# #         print(cookie)
# #     #5.是将dict转化成str格式
# #     jsonCookies = json.dumps(dictCookies)
# #     # 登录完成后,自动创建一个boss直聘.json的文件，将cookies保存到该环境根目录下
# #     with open(cookie文件名, "w") as fp:
# #         fp.write(jsonCookies)
# #         print('cookies保存成功！')
# # url='https://www.zhipin.com/web/geek/job-recommend'
# # 获取cookie(url,cookie文件名='boss直聘.json')
#
# import json
#
#
#
# import os
#
# # 指定要遍历的文件夹路径
# folder_path = '城市'  # 替换为您的文件夹路径
# index = 0
# # 遍历文件夹中的所有文件
# for filename in os.listdir(folder_path):
#     # 生成文件的完整路径
#     file_path = os.path.join(folder_path, filename)
#
#     with open(file_path, 'r', encoding='utf-8') as json_file:
#         data = json.load(json_file)  # 读取 JSON 数据
#         城市名 = data.get('zpData').get('businessDistrict').get('name')
#         城市 = data.get('zpData').get('businessDistrict').get('code')
#         subLevelModelList = data.get('zpData').get('businessDistrict').get('subLevelModelList')
#         所有区 = []
#         该城市所有区域={}
#         print(城市名)
#         for 区 in subLevelModelList:
#             当前区 = 所有区.append(区.get('code'))
#             print(区.get('code'))
#             if 区.get('subLevelModelList')!=None:
#                 所有区域 = []
#                 for 区域 in 区.get('subLevelModelList'):
#                     当前区域 = 所有区域.append(区域.get('code'))
#                     print(区域.get('code'))
#                     index = index+1
#                 该城市所有区域[区.get('code')] = 所有区域
#
#         print(城市名)
#         print(城市)
#         print(所有区)
#     print(该城市所有区域)
#     print("-----------------------------")
# print(index)
# # # ste = "13-5K"
# # # def calculate_average(ste):
# # #     # 提取数字部分
# # #     parts = ste.split('-')  # 根据 '-' 分割字符串
# # #     if len(parts) != 2:
# # #         raise ValueError("输入格式不正确，应该是 '数字-数字K'")
# # #
# # #     # 获取数字并转换为整数
# # #     num1 = int(parts[0])  # 第一个数字
# # #     num2 = int(parts[1][:-1])  # 第二个数字，去掉最后的 'K'
# # #
# # #     # 计算平均值
# # #     average = (num1 + num2) / 2
# # #     return average
# # # print(calculate_average(ste))
# # # import json
# # #
# # # # 准备要保存的数据
# # # data = {
# # #     "城市": 101020100,
# # #     "区": 310151,
# # #     "区域": 7377,
# # #     "page": 1
# # # }
# # #
# # # # 指定要保存的 JSON 文件路径
# # # file_path = 'data.json'  # 替换为您的文件路径
# # #
# # # # 使用覆盖的形式保存 JSON 文件
# # # with open(file_path, 'w', encoding='utf-8') as json_file:
# # #     json.dump(data, json_file, ensure_ascii=False, indent=4)  # 将数据写入文件
# # #
# # # print(f"数据已保存到 {file_path} 文件中。")
import json

城市名='上海'
城市数据 = {
    "城市": 城市名,
    "总共岗位数量": 1,
    "总薪资": 1,
    "平均薪资": 1,
    '需求证书岗位': 1,
    '岗位需求率': 1,
}
# 使用覆盖的形式保存 JSON 文件
with open(城市名, 'w', encoding='utf-8') as jsons:
    json.dump(城市数据, jsons, ensure_ascii=False, indent=4)  # 将数据写入文件