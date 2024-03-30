from django.http import JsonResponse


class ResponseMessage():
    # 成功
    @staticmethod
    def success(data):
        # 构造返回对象
        result = {
            "code":200,
            "msg":"操作成功",
            "data":data
        }
        # 以json形式来进行值的返回
        return JsonResponse(result,safe=False)
    # 失败
    @staticmethod
    def failed():
        result = {
            "code":500,
            "data": None,
            "msg": "操作失败",
        }
        return  JsonResponse(result,safe=False)

    # 其它
    @staticmethod
    def other(data):
        result = {
            "code":500,
            "data":None,
            "msg":data,
        }
        return JsonResponse(result,safe=False)

