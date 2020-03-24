from django.shortcuts import render,HttpResponse
from django.views.generic.base import View

class signin(View):
    def get(self,request):
        return HttpResponse("登录页面")
