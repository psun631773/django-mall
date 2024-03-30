"""
URL configuration for djangoMall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.category.views import TestView, CategoryAPIView, CategoryListAPIView, CategorySaveAPIView, \
    CategoryDeleteAPIView
from apps.SysUser.views import SysUserListAPIView

urlpatterns = [
    # 第二步 将路径和class类进行对应
    path('list', SysUserListAPIView.as_view()),
    # 分页查询
#     path('findPage', CategoryAPIView.as_view()),
#     # 新增和编辑
#     path('save', CategorySaveAPIView.as_view()),
#     # 单选和批量删除
#     path('delBatch', CategoryDeleteAPIView.as_view()),
]
