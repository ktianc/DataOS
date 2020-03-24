from django.urls import path
from . import views

app_name = 'cmsauth'

urlpatterns = [
    path('', views.signin.as_view(),name='signin'),
    path('signinauth/', views.signinauth,name='signinauth'),
]