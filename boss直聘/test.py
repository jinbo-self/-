import requests

URL = 'https://www.zhipin.com/job_detail/2c1ba0f36e5f882d1Hd43Nm4F1ZY.html'
res = requests.get(URL).text
print(res)