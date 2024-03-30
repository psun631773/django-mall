import get_content


print('请输入要爬取的页数：')
x = int(input())
for i in range(1,x+1):
    str = "https://www.uestcp.com.cn/shangpin-%d/"%i
    # print(str)
    print("正在爬取第一页：")
    print()
    get_content.get_tushu(str)


