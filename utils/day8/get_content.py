import requests
from lxml import etree
import pymysql
from pymysql import cursors

db = pymysql.connect(
    database="project",
    host='127.0.0.1',
    user = "root",
    password = "123456",
    cursorclass=cursors.DictCursor
)


def get_tushu(url):
    response = requests.get(url=url)

    # print(response.text)
    #
    # print((type(response.text)))
    #
    # print(response.content)
    #
    # print(type(response.content))


    #
    html = etree.HTML(response.content)
    #
    # print(html)
    #
    data = html.xpath("//div[@class='col-12 col-md-6 col-lg-4']")
    # print(html.xpath("//div[@class='subnav']/ul/li/a/text()"))
    #
    # print(data)
    # print(len(data))


    for i in data:
        # print(i)
        # print(i.xpath('./div/div/a/text()'))
        # print(i.xpath("./div/div[@class='product-name']/a/text()"))
        title = i.xpath("./div/div[@class='product-name']/a/text()")
        title = title[0]
        print('图书名称：%s'%title)

        # print(i.xpath("./div/div[@class='image']/a/img/@src"))
        picture = i.xpath("./div/div[@class='image']/a/img/@src")
        picture = 'https://www.uestcp.com.cn/'+picture[0]
        print("图书图片："+picture)

        star = i.xpath("./div/div[@class='about']/div[@class='rating']/img/@src")
        star = len(star)
        print("图书星级：%d"%star)


        price = i.xpath("./div/div[@class='about']/div[@class='price']/h3/text()")
        # print(price)
        price = price[0].replace('￥','')
        print("图书价格："+price)

        cursors = db.cursor()
        insert = (
            "insert into book(title,price,picture,star)"
            "values (%s,%s,%s,%s)"
        )
        data = (title, price, picture, star)
        cursors.execute(insert, data)

    # 关闭游标
    cursors.close()

    # 关闭连接
    db.commit()



#
# with open('nav.txt','w+',encoding='UTF-8') as f:
#     for i in html_xpath:
#         f.write(i+'\n')

# #获取路径
# file_path = os.getcwd()
# new_folder = file_path+'\\'+'图书图片\\'
# os.makedirs(new_folder)

# count = 0
# for i in data:



    # count = count + 1
    # print('正在下载第%d张图片'%count)
    #
    # img = requests.get(i).content
    # with open('{}%d.png'.format(new_folder)%count,'wb') as f:
    #
    #     # 写入图片数据
    #     f.write(img)
    #     f.close()
