from rest_framework import serializers

from apps.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    # 格式化输出时间
    create_time = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")
    update_time = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Category
        fields = "__all__"