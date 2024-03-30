import get_vagetable


print('请输入要爬取的页数,每页20个数据：')
x = int(input())
for i in range(1,x+1):
    str = "https://www.cnhnb.com/p/cjsl-0-0-0-0-%d/"%i

    # print(str)
    print("正在爬取第%d页："%i)
    print()
    get_vagetable.get_vage(str)


