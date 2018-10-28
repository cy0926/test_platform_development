from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from project_app.models import ProjectManage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# 主要的代码逻辑

def index(request):
    return render(request, 'index.html')


# 处理登录请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, 'index.html',
                          {"error": "用户名或密码为空"}
                          )
        else:
            # 验证用户是否存在
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)  # 验证登录
                request.session['user1'] = username
                return HttpResponseRedirect("/manage/project_manage/")
            else:
                return render(request, "index.html", {"error": "用户名密码错误"})
    else:
        return render(request, "index.html")


def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    return response
