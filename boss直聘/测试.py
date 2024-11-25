import time
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

# 设置 Edge 浏览器选项
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

    # 打印 cookies
    print("Cookies:", cookie_str)
    with open('Cookies', 'w', encoding='utf-8') as file:
        file.write(cookie_str)
    time.sleep(5)
finally:
    # 关闭浏览器
    driver.quit()