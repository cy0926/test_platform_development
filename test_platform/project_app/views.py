from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import ProjectManage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    return render(request, "project_manage.html", {"user1": username,
                                                   "projects": contacts})
