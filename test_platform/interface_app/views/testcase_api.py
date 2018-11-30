# -*-coding:utf-8-*-
from project_app.models import ProjectManage, Module
from interface_app.models import TestCase
from django.http import JsonResponse, HttpResponse
import json
import requests
from test_platform import common


def get_project_list(request):
    """
      获取项目模块列表
      :param request:
      :return: 项目接口列表
      """
    if request.method == "GET":
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

        return common.response_success(data=dataList)
    else:
        return common.response_failed("请求方法错误！")


def save_case(request):
    """
      保存接口测试用例
      :param request:
      :return:
    """
    if request.method == "POST":
        name = request.POST.get("name", "")
        url = request.POST.get("req_url", "")
        method = request.POST.get("req_method", "")
        parameter = request.POST.get("req_parameter", "")
        req_type = request.POST.get("req_type", "")
        header = request.POST.get("header", "")
        module_name = request.POST.get("module", "")
        assert_text = requests.POST.get("")

        if url == "" or method == "" or req_type == "" or module_name == "" or assert_text == "":
            return common.response_failed("必传参数为空")
        if parameter == "":
            parameter = "{}"
        if header == "":
            header = "{}"

        module_obj = Module.objects.get(title=module_name)
        case = TestCase.objects.create(name=name, module=module_obj, url=url,
                                       req_method=method, req_type=req_type,
                                       req_header=header, req_parameter=parameter,
                                       response_assert=assert_text)
        if case is not None:
            return common.response_success("保存成功!")

    else:
        return common.response_failed("请求方法错误!")


def api_debug(request):
    """
      HTTP接口调试
      :param request:
      :return: 接口调用结果
    """
    if request.method == 'POST':
        name = request.POST.get("name", "")
        url = request.POST.get("req_url", "")
        method = request.POST.get("req_method", "")
        parameter = request.POST.get("req_parameter", "")
        req_type = request.POST.get("req_type", "")
        header = request.POST.get("header", "")
        if url == "" or method == "" or req_type == "":
            return common.response_failed("必传参数不能为空")

        try:
            header_dict = json.loads(header.replace("'", "\""))
            payload = json.loads(parameter.replace("'", "\""))
        except json.decoder.JSONDecodeError:
            return common.response_failed("请检查 header 或参数的格式!")

        if method == "get":
            if req_type == "from":
                r = requests.get(url, headers=header_dict, params=payload)
            else:
                return common.response_failed("参数类型错误!")
        if method == "post":
            if req_type == "from":
                r = requests.post(url, data=payload)
            elif req_type == "json":
                r = requests.post(url, json=payload)
            else:
                return common.response_failed("参数类型错误!")
        return common.response_success(data=r.text)
    else:
        return common.response_failed("请求方法错误!")


def get_case_info(request):
    """
      获取接口数据
      :param request:
      :return:
    """
    if request.method == "POST":
        case_id = request.POST.get("caseId", "")
        print(case_id)
        if case_id == "":
            return common.response_failed("用例id为空")

        try:
            case_obj = TestCase.objects.get(id=case_id)
        except TestCase.DoesNotExist:
            return common.response_failed("查询用例不存在")

        # print("模块id：%s" % case_obj.module_id)
        # 通过module_id得到模块id
        mid = case_obj.module_id

        # 通过模块id得到模块对象
        module_obj = Module.objects.get(id=mid)
        # 通过模块对象得到模块名称
        module_name = module_obj.title

        pid = module_obj.project_id
        # print("项目id:%s" % pid)

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
            "assertText": case_obj.response_assert
        }
        return common.response_success(data=case_info)

    else:
        return common.response_failed("请求方法错误!")


def api_assert(request):
    """
    对测试用例的断言进行验证
    :param request:
    :return:
    """
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")

        if result_text == "" or assert_text == "":
            return common.response_failed("验证的数据不能为空")

        try:
            assert assert_text in result_text
        except AssertionError:
            return common.response_failed("验证失败!")
        else:
            return common.response_failed("验证成功!")
    else:
        return common.response_failed("请求方法错误")


def update_case(request):
    """
    更新接口测试用例
    :param request:
    :return:
    """
    if request.method == "POST":
        case_id = request.POST.get("cid", "")
        name = request.POST.get("name", "")
        url = request.POST.get("req_url", "")
        method = request.POST.get("req_method", "")
        parameter = request.POST.get("req_parameter", "")
        req_type = request.POST.get("req_type", "")
        header = request.POST.get("header", "")
        module_name = request.POST.get("module", "")
        assert_text = request.POST.get("assert_text", "")
        # print("用例id:", case_id)

        if url == "" or method == "" or req_type == "" or module_name == "" or assert_text == "":
            return common.response_failed("必传参数为空")
        if parameter == "":
            parameter = "{}"
        if header == "":
            header = "{}"

        module_obj = Module.objects.get(title=module_name)
        # 更新数据（更新对应id的数据）
        case_obj = TestCase.objects.filter(id=case_id).update(
            module=module_obj,
            name=name,
            url=url,
            req_method=method,
            req_header=header,
            req_type=req_type,
            req_parameter=parameter,
            response_assert=assert_text
        )
        if case_obj == 1:
            return common.response_success("更新成功!")
        else:
            return common.response_failed("更新失败!")
    else:
        return common.response_failed("请求方法错误")
