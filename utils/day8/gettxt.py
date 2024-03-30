import requests
from lxml import etree

response = requests.get(url='http://meyapp.com/meiwen/13279.html')


html = etree.HTML(response.content)

print(html)

html_xpath = html.xpath("//div[@class='subnav']/ul/li/a/text()")
print(html.xpath("//div[@class='subnav']/ul/li/a/text()"))

for i in html_xpath:
    print(i)

with open('nav.txt','w+',encoding='UTF-8') as f:
    for i in html_xpath:
        f.write(i+'\n')