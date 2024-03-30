import json
import re

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from lxml import etree
from rest_framework.views import APIView

from apps.category.CagetorySerializer import CategorySerializer
from apps.category.models import Category
from apps.common import ResponseMessage
from djangoMall.settings import PAGE_SIZE
import logging

# Create your views here.

class TestView(View):
    # get请求
    def get(self,request):
        # 获取category表中的全部数据
        list = Category.objects.all()

        # 将查询结果序列化为json格式
        serializer = CategorySerializer(list,many=True)
        print(serializer)
        return JsonResponse(serializer.data,safe=False)
    def post(self,request):
        # 在控制台输出
        print("post请求")
        # 通过requests库获取网页源代码
        response = requests.get("https://www.cnhnb.com/p/cjsl/")
        # 编码问题 指定编码格式为utf-8编码
        html = etree.HTML(response.content.decode("UTF-8"))

        # 获取当前页面所有class类为supply-item项
        data = html.xpath("//a[@class='col-item-a']/text()")
        print(data)
        for item in data:
            # 匹配换行符
            item = re.sub(r"\n","",item)
            item = item.replace(" ","")
            print(item)
            # 定义插入的字段
            obj = Category(title=item)
            # 调用保存方法
            obj.save()

        # 返回数据
        return HttpResponse("post请求")

# 第一步 编写一个接口
# 分类分页接口
class CategoryAPIView(APIView):

    # 该接口需要通过post来进行访问
    # def get(self,request):
    #     # 查询操作 list表示的是category对象
    #     list = Category.objects.all()
    #     # 将对象转换为json
    #     serializer = CategorySerializer(list,many=True)
    #     # 将JSON列表返回给前端，如果返回的对象是一个字段，那么不需要添加safe
    #     return JsonResponse(serializer.data,safe=False)

    def get(self,request):
        # get获取前端传入的参数
        page_num = request.GET.get("pageNum")
        print(page_num)
        # 定义返回字典
        data = {
            "msg":"GET请求分页查询", # 用来提示信息
            "data":"前端传入的参数值为：{}".format(page_num), # 用来存放返回的数据
            "code":200 #code表示状态码
        }
        # return JsonResponse(data)
        # return ResponseMessage.ResponseMessage.success(page_num) #成功
        #return ResponseMessage.ResponseMessage.failed() #失败
        return ResponseMessage.ResponseMessage.other("用户名密码错误") #其它

    def post(self,request):
        # 定义返回字典
        # 接收前端传输的对象
        data = request.data
        #获取前端传输的pageNum字段
        page = data.get("pageNum")
        # current
        # current_page = (page-1) * 2
        # 开始
        current_page = (page-1) * PAGE_SIZE
        # 结束
        end_page  =page* PAGE_SIZE
        """
        当page=1 size=2 current_page=0  end_page=2
        当page=2 size=2 current_page=2  end_page=4
        当page=3 size=2 current_page=4  end_page=6
        """
        list = Category.objects.all()[current_page:end_page]
        # 创建CategorySerializer实例 将查询结果序列化为json格式
        serializer = CategorySerializer(list,many=True)
        # 返回分类列表和分页总数 变量颜色是灰色的，表示该变量没有被使用
        result_list = {
            "list": serializer.data, # 获取分类列表
            "total": Category.objects.count() # 通过ORM中提供的count方法，获取数据库该表数据总数
        }
        return ResponseMessage.ResponseMessage.success(result_list)


class CategoryListAPIView(APIView):

    # 该接口需要通过post来进行访问
    def get(self,request):
        # 查询操作 list表示的是category对象
        list = Category.objects.all()
        # 将对象转换为json
        serializer = CategorySerializer(list,many=True)
        # 将JSON列表返回给前端，如果返回的对象是一个字段，那么不需要添加safe
        return JsonResponse(serializer.data,safe=False)

class CategorySaveAPIView(APIView):
    def post(self,request):
        # 获取post请求参数
        data = request.data
        # 获取id
        id = data.get("id")
        # 如果id存在 编辑
        if id:
            # 通过ORM的get方法，通过数据的id来查询数据
            instance = Category.objects.get(id=id)
            # 对实例进行序列化操作，instance实例对象 data数据对象 partial允许部分字段更新
            serializer = CategorySerializer(instance,data=data,partial=True)
            # is_valid方法用来对数据做验证 需要在序列化器里面编写验证规则
            if serializer.is_valid():
                # 调用save方法来对数据进行保存操作
                serializer.save()
                return ResponseMessage.ResponseMessage.success(None)
        else:
            # 不存在ID 则是新增操作
            serializer = CategorySerializer(data = data)
            # 验证参数是否符合要求
            if serializer.is_valid():
                # 符合要求，数据进行保存
                serializer.save()
                # 返回成功状态下数据
                return ResponseMessage.ResponseMessage.success(None)
            else:
                # 返回失败状态下数据
                return ResponseMessage.ResponseMessage.failed()

class CategoryDeleteAPIView(APIView):
    def post(self,request):
        print(type(request.body)) # <class 'bytes'>
        # 将json格式的字符串转换Python对象
        data = json.loads(request.body)
        print(type(data)) # <class 'list'>
        print(data)
        # 获取数据 循环遍历
        for id in data:
            # 方法1
            # print("当前需要删除的ID为：{}".format(id))
            # 方法2
            print("当前需要删除的ID为："+ str(id))
            try:
                #可能存在异常的语句

                # 通过ORM的get方法查询出该条数据 数据未找到，会抛出异常
                category = Category.objects.get(id=id)
                # 将该条数据删除
                category.delete()
            except Category.DoesNotExist:
                # 触发DoesNotExist异常执行的语句
                logging.error('没有找到需要删除的数据')
                return ResponseMessage.ResponseMessage.other("没有找到需要删除的数据")
        # 循环获取值
        return ResponseMessage.ResponseMessage.success(None)