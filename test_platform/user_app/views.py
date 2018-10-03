from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from user_app.models import ProjectManage
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
                return HttpResponseRedirect("/project_manage/")
            else:
                return render(request, "index.html", {"error": "用户名密码错误"})
    else:
        return render(request, "index.html")


# 项目管理页面
@login_required
def project_manage(request):
    username = request.session.get('user1', '')  # 读取浏览器 cookies
    # project_list = ProjectManage.objects.all()
    project_list = ProjectManage.objects.get_queryset().order_by('id')
    paginator = Paginator(project_list, 2)
    # print(paginator.count)
    page = request.GET.get("page")
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "project_manage.html", {"user1": username,
                                                   "projects": contacts})


# 项目管理页面的搜索
@login_required()
def search(request):
    if request.method == "GET":
        search = request.GET.get("search", "")
        search_list = ProjectManage.objects.filter(title__contains=search)
        username = request.session.get('user1', '')  # 读取浏览器 cookies
        return render(request, "project_manage.html", {"user1": username,
                                                       "projects": search_list})


def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    return response
