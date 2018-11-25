import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from interface_app.models import TestCase
from project_app.models import ProjectManage, Module
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from interface_app.forms import TestCaseForm
from project_app.forms import ProjectForm, ModuleForm


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
def add_case(request):
    if request.method == "GET":
        # 这里的form表单应该暂时没用到
        form = TestCaseForm()
        return render(request, "add_case.html", {
            "form": form,
            "type": "add"
        })
    else:
        return HttpResponse("404")


# 添加/编辑用例的“调试”按钮
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
        else:
            header = json.loads(header.replace("'", "\""))

        if method == "get":
            r = requests.get(url, params=parameter)
        if method == "post":
            r = requests.post(url, json=parameter, headers=header)

        return HttpResponse(r.text)


# 保存用例
def save_case(request):
    """
    保存用例
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


# 用例列表--针对单个用例的“调试”功能
def debug_case(request, case_id):
    if request.method == "GET":
        # 这里的form表单应该暂时没用到
        form = TestCaseForm(request.POST)
        return render(request, 'debug_case.html',
                      {'form': form,
                       'type': 'edit'})
    else:

        return HttpResponse('404')


# 获取用例信息的接口
def get_case_info(request):
    if request.method == "POST":
        case_id = request.POST.get("caseId", "")
        print(case_id)
        if case_id == "":
            return JsonResponse({"success": "false",
                                 "message": "case_id is null."})
        case_obj = TestCase.objects.get(id=case_id)

        print("模块id：%s" % case_obj.module_id)
        mid = case_obj.module_id

        module_obj = Module.objects.get(id=mid)
        module_name = module_obj.title

        pid = module_obj.project_id
        print("项目id:%s" % pid)

        project_obj = ProjectManage.objects.get(id=pid)
        project_name = project_obj.title

        case_info = {
            "module_name": module_name,
            "project_name": project_name,
            "name": case_obj.name,
            "url": case_obj.url,
            "req_method": case_obj.req_method,
            "req_type": case_obj.req_type,
            "req_header": case_obj.req_header,
            "req_parameter": case_obj.req_parameter,
        }
        return JsonResponse({"success": "true",
                             "message": "ok",
                             "data": case_info})

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
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request, "case_manage.html", {'cases': contacts,
                                                    'type': "list",
                                                    'search': search})


# 删除用例
def delete_case(request, case_id):
    TestCase.objects.filter(id=case_id).delete()
    return HttpResponseRedirect('/interface/case_manage/')
