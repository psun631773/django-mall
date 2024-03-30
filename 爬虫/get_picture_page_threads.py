import os
import threading

import requests
from lxml import etree

# 要爬取的网页列表
# url_list = ['http://www.example.com/page1', 'http://www.example.com/page2', 'http://www.example.com/page3']

# 获取当前文件路径
file = os.getcwd()
print(file)
new_folder = file + "\\" + "图片文件夹\\"
if os.path.exists(new_folder):
    raise Exception('%s 已经存在不可创建' % new_folder)
os.makedirs(new_folder)

url_list = []
for i in range(1, 20):
    url_list.append("https://www.keaitupian.cn/fengjing/list_2_" + str(i) + ".html")

# 爬取函数
def fetch_url(url, i):
    print("当前为第{}页".format(i + 1))
    # 创建外围文件夹
    new_folder = file + "\\" + "图片文件夹\\"
    new_folder = new_folder + "\\" + str(i) + "\\"
    if os.path.exists(new_folder):
        raise Exception('%s 已经存在不可创建' % new_folder)
    os.makedirs(new_folder)

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

# 创建线程
threads = []
for index, url in enumerate(url_list):
    t = threading.Thread(target=fetch_url, args=(url, index))
    threads.append(t)

# 启动线程
for t in threads:
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print('所有网页已经爬取完毕！')
