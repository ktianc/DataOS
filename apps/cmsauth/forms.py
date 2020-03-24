from django.forms import *
from apps.forms import FormMixin

class signinauth_form(Form,FormMixin):
    username = CharField(max_length=11)
    password = CharField(max_length=20, min_length=6,error_messages={"max_length":"密码最多不能超过20个字符！","min_length":"密码最少不能少于6个字符！"})
    remember = IntegerField(required=False)