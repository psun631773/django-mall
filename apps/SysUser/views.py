from django.shortcuts import render

from apps.common.ResponseMessage import ResponseMessage
from rest_framework.views import APIView
from apps.SysUser.SysUserSerializer import SysUserSerializer
from apps.SysUser.models import SysUser
# Create your views here.

class SysUserListAPIView(APIView):
    def get(self,request):
        print('用户列表获取')

        list = SysUser.objects.all()
        print((type(list)))
        serializer = SysUserSerializer(list,many = True)

        return ResponseMessage.success(serializer.data)