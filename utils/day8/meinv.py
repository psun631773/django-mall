import os

import requests
from lxml import etree

response = requests.get(url='https://www.keaitupian.cn/meinv/')

html = etree.HTML(response.content)


data = html.xpath("//img/@src")
print(data)

#获取路径
file_path = os.getcwd()
new_folder = file_path+'\\'+'美女图片\\'
os.makedirs(new_folder)

count = 0
for i in data:
    count = count + 1
    print('正在下载第%d张图片'%count)
    if count == 1:
        i = 'https://www.keaitupian.cn' + i

    img = requests.get(i).content
    with open('{}%d.png'.format(new_folder)%count,'wb') as f:

        # 写入图片数据
        f.write(img)
        f.close()

# with open('nav.txt','w+',encoding='UTF-8') as f:
#     for i in data:
#         f.write(i+'\n')
#
# with open('tp1.png','wb') as f:
#     f.write(response.content)