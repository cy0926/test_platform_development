from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Module
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from project_app.forms import ModuleForm


# 模块管理页面
@login_required
def module_manage(request):
    username = request.session.get('user1', '')  # 读取浏览器cookies
    manage_list = Module.objects.get_queryset().order_by('id')
    paginator = Paginator(manage_list, 10)
    # print(paginator.count)
    page = request.GET.get("page")
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "module_manage.html", {"user": username,
                                                  "modules": contacts,
                                                  "type": "list"
                                                  })


# 添加模块
def add_module(request):
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            project = form.cleaned_data['project']
            Module.objects.create(title=title, description=description, project=project)
            return HttpResponseRedirect('/manage/module_manage/')
    else:
        form = ModuleForm()

    return render(request, "module_manage.html", {"form": form,
                                                  "type": "add"
                                                  })


# 编辑模块
def edit_module(request, mid):
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            modle = Module.objects.get(id=mid)
            modle.title = form.cleaned_data['title']
            modle.description = form.cleaned_data['description']
            modle.project = form.cleaned_data['project']
            modle.save()
            return HttpResponseRedirect('/manage/module_manage/')
    else:
        form = ModuleForm(instance=Module.objects.get(id=mid))

    return render(request, "module_manage.html", {"form": form,
                                                  "type": "edit"
                                                  })


# 删除模块
def delete_module(request, mid):
    Module.objects.get(id=mid).delete()
    return HttpResponseRedirect('/manage/module_manage/')
