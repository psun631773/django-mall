import requests

#通过request,访问网址数据
response = requests.get('http://httpbin.org/ip')

#打印数据
print(response.text)