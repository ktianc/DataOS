from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views.generic.base import View
from django.views.decorators.http import require_POST
from .forms import signinauth_form
from django.contrib.auth import authenticate, login, logout
from utils import restful

class signin(View):
    def get(self,request):
        return render(request,'auth/login.html')
    def post(self,request):
        form = signinauth_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            remember = form.cleaned_data.get("remember")
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    # 登录成功以后判断，是否为记住密码，记住密码的话 将session保留两周，不记住密码，到浏览器结束自动删除
                    if remember:
                        request.session.set_expiry(None)
                    else:
                        request.session.set_expiry(0)
                    # 最后返回json数据
                    return redirect(reverse("cms:index"))
                # else：返回json数据,错误信息
                else:
                    return restful.blocked(message="账户被冻结")
            else:
                return restful.paramerror(message="用户名或密码错误")
            # 返回json数据  中 带有表单报错信息
        else:
            return restful.paramerror(message=form.get_errors())

@require_POST
def signinauth(request):
    form = signinauth_form(require_POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        remember = form.cleaned_data.get("remember")
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # 登录成功以后判断，是否为记住密码，记住密码的话 将session保留两周，不记住密码，到浏览器结束自动删除
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                # 最后返回json数据
                return restful.ok(message="登录成功")
            # else：返回json数据,错误信息
            else:
                return restful.blocked(message="账户被冻结")
        else:
            return restful.paramerror(message="用户名或密码错误")
        # 返回json数据  中 带有表单报错信息
    else:
        return restful.paramerror(message=form.get_errors())
