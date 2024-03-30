import requests
from lxml import etree


# 通过requests库获取网页源代码
response = requests.get("https://www.cnhnb.com/p/cjsl/")
# 编码问题 指定编码格式为utf-8编码
html = etree.HTML(response.content.decode("UTF-8"))


# 获取当前页面所有class类为supply-item项
data = html.xpath("//div[@class='supply-item']/div/a/div/div[@class='title-field']/div/h2/text()")
print(data)
for item in data:
    print(item)


