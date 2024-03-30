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


def get_vage(url):
    response = requests.get(url=url)

    # print(response.text)
    #
    # print((type(response.text)))
    #
    # print(response.content)
    #
    # print(type(response.content))


    #
    html = etree.HTML(response.content.decode("UTF-8"))
    #
    # print(html)
    #
    data = html.xpath("//div[@class='supply-item']")
    # print(html.xpath("//div[@class='subnav']/ul/li/a/text()"))
    #
    print(data)
    # print(len(data))


    for i in data:
        print(i)
        # print(i.xpath('./div/div/a/text()'))
        # print(i.xpath("./div/div[@class='product-name']/a/text()"))
        title = i.xpath("./div/a/div/div/div[@class='title']/h2/text()")
        title = title[0]
        print('蔬菜名称：%s'%title)

        # # print(i.xpath("./div/div[@class='image']/a/img/@src"))
        picture = i.xpath("./div/a/div/div[@class='shop-image']/img/@src")
        picture = picture[0]
        # picture = 'https://www.uestcp.com.cn/'+picture[0]
        print("蔬菜图片："+picture)
        #
        price = i.xpath("./div/a/div/div/div/div[@class='shops-price']/span/text()")
        price = price[0]+"元/斤"
        print("蔬菜单价："+price)
        # print("图书星级：%d"%price)
        #
        #
        company = i.xpath("./div/a/div/div/div[@class='l-shop-btm']/a/text()")
        # print(path)
        company = company[0]
        print("公司："+company)

        gspath = i.xpath("./div/a/div/div/div[@class='r-shop-btm']/text()")
        # print(path)
        gspath = gspath[0]
        print("地址："+gspath)

        cursors = db.cursor()
        insert = (
            "insert into vagetable(title,price,picture,company,gspath)"
            "values (%s,%s,%s,%s,%s)"
        )
        data = (title, price, picture, company,gspath)
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
