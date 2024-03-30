from rest_framework import serializers

from apps.category.models import Category
from apps.SysUser.models import SysUser

class SysUserSerializer(serializers.ModelSerializer):
    # 格式化输出时间
    # create_time = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")
    # update_time = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")

    class Meta:
        model = SysUser
        fields = "__all__"