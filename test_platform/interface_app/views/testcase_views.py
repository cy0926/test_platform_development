from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from interface_app.models import TestCase
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from interface_app.forms import TestCaseForm


# 用例管理页面（获取用例列表）
def case_manage(request):
    # 直接用objects.all()，分页的是会报错，所以用了order_by
    # cases_list = TestCase.objects.all()
    tasks_list = TestCase.objects.get_queryset().order_by('id')
    paginator = Paginator(tasks_list, 10)

    page = request.GET.get("page")
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)

    if request.method == "GET":
        return render(request, "case_manage.html", {
            "cases": contacts,
            "type": "list"})
    else:
        return HttpResponse("404")


# 用例列表--点击“添加用例”按钮
def add_case(request):
    if request.method == "GET":
        # 这里的form表单应该暂时没用到
        # form = TestCaseForm()
        return render(request, "add_case.html", {
            # "form": form,
            "type": "add"
        })
    else:
        return HttpResponse("404")


# 用例列表--针对单个用例的“调试”功能
def debug_case(request, case_id):
    if request.method == "GET":
        # 这里的form表单应该暂时没用到
        # form = TestCaseForm(request.POST)
        return render(request, 'debug_case.html', {
            # 'form': form,
            'type': 'edit'
        })
    else:

        return HttpResponse('404')


# 用例搜索
def search_case_name(request):
    if request.method == "GET":
        # 获取搜索关键字
        search = request.GET.get("case_name", "")
        search_list = TestCase.objects.filter(name__contains=search)

        paginator = Paginator(search_list, 10)
        # 获取当前页码
        page = request.GET.get("page")
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # 如果页数不是整型, 取第一页.
            contacts = paginator.page(1)
        except EmptyPage:
            # 如果页数超出查询范围，取最后一页
            contacts = paginator.page(paginator.num_pages)
        return render(request, "case_manage.html", {
            'cases': contacts,
            'type': "list",
            'search': search
        })
    else:
        return HttpResponse('404')


# 删除用例
def delete_case(request, case_id):
    TestCase.objects.filter(id=case_id).delete()
    return HttpResponseRedirect('/interface/case_manage/')
