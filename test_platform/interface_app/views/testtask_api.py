# -*-coding:utf-8-*-
from test_platform import common
from interface_app.models import TestTask


# 保存任务
def save_task_data(request):
    if request.method == "POST":
        name = request.POST.get("task_name", "")
        describe = request.POST.get("task_describe", "")
        cases = request.POST.get("task_cases", "")

        if name == "":
            return common.response_failed("任务名称不能为空！")

        # 保存数据库
        task = TestTask.objects.create(name=name,describe=describe,cases=cases)
        if task is None:
            return common.response_failed("任务创建失败！")
        else:
            return common.response_success("任务创建成功~！")
    else:
        return common.response_failed("请求方法错误！")
