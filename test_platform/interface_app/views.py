import json
import requests
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# 用例管理页面
def case_manage(request):
    if request.method == "GET":
        return render(request, "case_manage.html",
                      {"type": "list"}
                      )
    else:
        return HttpResponse("404")


# 用例列表--点击“调试”按钮
def debug(request):
    if request.method == "GET":
        return render(request, "api_debug.html")
    else:
        return HttpResponse("404")


# 调试
def api_debug(request):
    if request.method == 'POST':
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        parameter = request.POST.get("req_parameter")

        paylod = json.loads(parameter.replace("'", "\""))

        if method == "get":
            r = requests.get(url, params=paylod)
        if method == "post":
            r = requests.post(url, json=paylod)
        return HttpResponse(r.text)
