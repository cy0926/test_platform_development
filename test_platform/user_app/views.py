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


# 项目管理页面的搜索(通过title搜索)
@login_required()
def search(request):
    if request.method == "GET":
        username = request.session.get('user1', '')  # 读取浏览器 cookies
        search = request.GET.get("search", "")
        search_list = ProjectManage.objects.filter(title__contains=search)
        paginator = Paginator(search_list, 10)

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        return render(request, "project_manage.html", {"user1": username,
                                                       "projects": contacts,
                                                       "search": search})


# 添加项目页面
def add_index(request):
    return render(request, 'add_index.html')


# 添加项目操作
def add_project(request):
    # username = request.session.get('user1', '')  # 读取浏览器 cookies
    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        status = request.POST.get('status')
        if status is True:
            status = 1
        else:
            status = 0
        if title == "" or description == "":
            return render(request, "add_index.html",
                          {"error": "名称和描述必填"}
                          )
        else:
            ProjectManage.objects.create(title=title, description=description, status=status)
            response = HttpResponseRedirect('/project_manage/')
            return response


# 删除项目
def delete_project(request, project_id):
    ProjectManage.objects.filter(id=project_id).delete()
    response = HttpResponseRedirect('/project_manage/')
    return response


# 编辑项目页面
def edit_project_page(request, project_id):
    project = ProjectManage.objects.get(pk=project_id)
    print(project)
    edit_title = project.title
    edit_description = project.description
    edit_status = project.status
    project_id = project.id
    return render(request, 'edit_project_page.html',
                  {"edit_title": edit_title,
                   "edit_description": edit_description,
                   "project_id": project_id,
                   "edit_status": edit_status
                   })


# 编辑项目之后的提交操作
def edit_project_action(request, project_id):
    project = ProjectManage.objects.get(pk=project_id)
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    status = request.POST.get('status')
    if status is True:
        status = 1
    else:
        status = 0
    project.title = title
    project.description = description
    project.status = status
    project.save()
    response = HttpResponseRedirect('/project_manage/')
    return response


def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    return response
