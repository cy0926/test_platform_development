import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from interface_app.models import TestCase
from project_app.models import ProjectManage, Module
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# 获取项目，模块列表
def get_project_list(request):
    project_list = ProjectManage.objects.all()
    dataList = []
    for project in project_list:
        project_dict = {
            "name": project.title
        }
        module_list = Module.objects.filter(project_id=project.id)
        if len(module_list) != 0:
            module_name = []
            for module in module_list:
                module_name.append(module.title)

            project_dict["moduleList"] = module_name
            dataList.append(project_dict)

    return JsonResponse({"success": "true", "data": dataList})


# 用例管理页面
def case_manage(request):
    cases_list = TestCase.objects.get_queryset().order_by('id')
    paginator = Paginator(cases_list, 10)
    page = request.GET.get("page")
    try:
        contacts = paginator.page(page)

    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "case_manage.html",
                  {"cases": contacts,
                   "type": "list"})


# 用例列表--点击“添加用例”按钮
def debug(request):
    if request.method == "GET":
        return render(request, "api_debug.html")
    else:
        return HttpResponse("404")


# 调试
def api_debug(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        url = request.POST.get("req_url", "")
        method = request.POST.get("req_method", "")
        parameter = request.POST.get("req_parameter", "")
        req_type = request.POST.get("req_type", "")
        header = request.POST.get("header", "")

        if parameter == "":
            parameter = "{}"
        else:
            parameter = json.loads(parameter.replace("'", "\""))

        if header == "":
            header = "{}"

        if method == "get":
            r = requests.get(url, params=parameter)
        if method == "post":
            r = requests.post(url, json=parameter)

        return HttpResponse(r.text)


# 保存用例
def save_case(request):
    """
    保存用例
    :param request:
    :return:


    "name": name,
    "req_url" :url,
    "req_method" : method,
    "req_parameter": parameter,
    "req_type": req_type,
    "header": header,
    """
    if request.method == "POST":
        name = request.POST.get("name", "")
        url = request.POST.get("req_url", "")
        method = request.POST.get("req_method", "")
        parameter = request.POST.get("req_parameter", "")
        req_type = request.POST.get("req_type", "")
        header = request.POST.get("header", "")
        module_name = request.POST.get("module", "")

        if url == "" or method == "" or req_type == "":
            return HttpResponse("必传参数为空")
        if parameter == "":
            parameter = "{}"
        if header == "":
            header = "{}"

        module_obj = Module.objects.get(title=module_name)
        case = TestCase.objects.create(name=name, module=module_obj, url=url, req_method=method,
                                       req_type=req_type, req_header=header, req_parameter=parameter)
        if case is not None:
            return HttpResponse("保存成功")

    else:
        return HttpResponse("404")


# 编辑用例
def edit_case(request, case_id):
    pass
