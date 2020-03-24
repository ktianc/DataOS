from django.shortcuts import render,HttpResponse
from django.views.generic.base import View

class index(View):
    def get(self,request):
        return HttpResponse("管理页面主页")