from interface_app.models import TestTask, TestCase
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
说明：借口任务文件，返回 HTML 页面
"""


# 用例管理页面（获取用例列表）
def task_manage(request):
    # 直接用objects.all()，分页的是会报错，所以用了order_by
    # cases_list = TestCase.objects.all()
    cases_list = TestTask.objects.get_queryset().order_by('id')
    paginator = Paginator(cases_list, 10)

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
        return render(request, "task_manage.html", {
            "tasks": contacts,
            "type": "list"
        })
    else:
        return HttpResponse("404")


def search_task_name(request):
    if request.method == "GET":
        # 获取搜索关键字
        search = request.GET.get("task_name", "")
        search_list = TestTask.objects.filter(name__contains=search)

        paginator = Paginator(search_list, 10)
        # 获取当前页码
        page = request.GET.get("page")

        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        return render(request, "task_manage.html", {
            "tasks": contacts,
            "type": "list",
            "search": search
        })


# 创建任务
def add_task(request):
    if request.method == "GET":
        return render(request, "add_task.html", {
            "type": "add",
        })


# 获取任务对应的用例数据
def run_task(request, tid):
    if request.method == "GET":
        task_obj = TestTask.objects.get(id=tid)
        cases_list = task_obj.cases.split(",")
        cases_list.pop(-1)
        # print(cases_list)
        all_cases_dict = {}
        for case_id in cases_list:
            case_obj = TestCase.objects.get(id=case_id)
            case_dic = {
                "url": case_obj.url,
                "method": case_obj.req_method,
                "type_": case_obj.req_type,
                "header": case_obj.req_header,
                "parameter": case_obj.req_parameter,
                "assert_": case_obj.response_assert
            }
            all_cases_dict[case_obj.id] = case_dic

        print(all_cases_dict)
    else:
        return HttpResponse("404")
