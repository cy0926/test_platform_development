from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def case_manage(request):
    if request.method == "GET":
        return render(request, "case_manage.html")
    else:
        return HttpResponse('404')

