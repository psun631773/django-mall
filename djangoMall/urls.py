"""djangoMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.category.views import TestView

# 第三步 配置项目信息
schema_view = get_schema_view(
    openapi.Info(
        # api 标题
        title="Django+Vue智慧商城项目",
        default_version='v1.0.1',
        description="这是一个基于Django+Vue的前后端分离智慧商城项目，有阿里支付等功能",
        terms_of_service="https://www.xxx.com/project/",
        contact=openapi.Contact(email="163@163.com"),
        license=openapi.License(name="版权所有"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # test/表示的是访问路径 TestView.as_view()该路径调用的python方法
    path("test/",TestView.as_view()),
    # 第三步 引入模块
    # 路由路径 引入的模块
    path("category/", include("apps.category.urls")),
    path("a/", include("apps.category.urls")),
    path("b/", include("apps.category.urls")),
    #cache_timeout 缓存时间
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('sysUsers/',include("apps.SysUser.urls"))
]
