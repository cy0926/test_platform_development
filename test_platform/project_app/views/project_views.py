from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import ProjectManage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from project_app.forms import ProjectForm


# Create your views here.
# 项目管理页面
@login_required
def project_manage(request):
    username = request.session.get('user1', '')  # 读取浏览器 cookies
    # project_list = ProjectManage.objects.all()
    project_list = ProjectManage.objects.get_queryset().order_by('id')
    paginator = Paginator(project_list, 10)
    # print(paginator.count)
    page = request.GET.get("page")
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "project_manage.html", {"user": username,
                                                   "projects": contacts,
                                                   "type": "list"})


# 添加项目操作
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            ProjectManage.objects.create(title=title, description=description, status=status)
            return HttpResponseRedirect('/manage/project_manage/')
    else:
        form = ProjectForm()

    return render(request, 'project_manage.html',
                  {'form': form,
                   'type': "add"})


# 编辑项目页面
def edit_project(request, pid):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = ProjectManage.objects.get(id=pid)
            project.title = form.cleaned_data['title']
            project.description = form.cleaned_data['description']
            project.status = form.cleaned_data['status']
            project.save()
            return HttpResponseRedirect('/manage/project_manage/')
    else:
        if pid:
            form = ProjectForm(
                instance=ProjectManage.objects.get(id=pid)
            )
    return render(request, 'project_manage.html',
                  {'form': form,
                   'type': "edit"})


# 删除项目
def delete_project(request, pid):
    ProjectManage.objects.filter(id=pid).delete()
    response = HttpResponseRedirect('/manage/project_manage/')
    return response


# 项目管理页面的搜索(通过title搜索)
@login_required
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
                                                       "search": search,
                                                       "type": "list"})
