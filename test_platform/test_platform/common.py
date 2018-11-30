# -*-coding:utf-8-*-
from django.http import JsonResponse


def response_success(message="请求成功", data={}):
    content = {
        "success": "true",
        "message": message,
        "data": data
    }
    return JsonResponse(content)


def response_failed(message="参数错误"):
    content = {
        "success": "false",
        "message": message
    }
    return JsonResponse(content)
