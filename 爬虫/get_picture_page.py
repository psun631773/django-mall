import os

import pymysql
import requests
from lxml import etree

from pymysql import cursors

# 图书爬取并存入数据库 http://www.uestcp.com.cn/shangpin/


# 获取当前文件路径
file = os.getcwd()
print(file)
new_folder = file + "\\" + "图片文件夹2\\"
if os.path.exists(new_folder):
    raise Exception('%s 已经存在不可创建' % new_folder)


for i in range(1,20):
    print("当前为第{}页".format(i))
    # 创建外围文件夹
    new_folder = file + "\\" + "图片文件夹\\"
    new_folder = new_folder+"\\"+str(i)+"\\"
    if os.path.exists(new_folder):
        raise Exception('%s 已经存在不可创建' % new_folder)
    os.makedirs(new_folder)
    url = "https://www.keaitupian.cn/fengjing/list_2_"+str(i)+".html"
    response = requests.get(url)
    print(type(response))
    html = etree.HTML(response.content)
    data = html.xpath("//li[@class='related_box']")
    count = 0
    for item in data:
        count = count + 1
        # .非常重要，代表上一层级
        # 标题
        # title = item.xpath("./div/div/a/text()")
        # 图片
        img = item.xpath("./a/img/@src")
        # img = "http://www.uestcp.com.cn/" + img[0]
        print(img[0])
        response = requests.get(url=img[0])
        # 访问图片的二进制数据
        # print(response.content)

        file_name = new_folder + str(count) + ".jpg"
        with open(file_name, "wb") as f:
            # 写入图片数据
            f.write(response.content)
            f.close()