### django cookie的使用
参考： https://docs.djangoproject.com/en/2.1/ref/request-response/ https://docs.djangoproject.com/en/2.1/topics/http/sessions/

设置cookie
当你想把数据保存到浏览器cookie时，可以使用set_cookie()方法
```
from django.http import HttpResponseRedirect, HttpResponse

# ……
response = HttpResponse()
response.set_cookie('user', username, 3600) # 添加浏览器cookie
return response

#或者
response = HttpResponseRedirect('/event_manage/')
response.set_cookie('user', username, 3600)   # 添加浏览器cookie
return response

```
3600为失效时间，单位：秒
如果想获取浏览器cookie
```
def manage(request):
    username = request.COOKIES.get('user', '') # 读取浏览器cookie
```

设置session
当然也可以通过session，保存在浏览器中的将不再是数据本身，而是数据的sessionid。通过Sessionid到服务器端口获取真正的数据，这样将大大提高安全性
```
from django.http import HttpResponseRedirect, HttpResponse
# ....
    request.session['user'] = username   # 将session信息记录到浏览器
    return HttpResponde() 
```

如果想获取浏览器的session:
```
def manage(request):
    username = request.session.get('user', '')  # 读取浏览器session
```
session的失效时间可以在settings.py中设置
```
  SESSION_COOKIE_AGE = 3600
```
单位为：秒
