from django.urls import path, re_path
from app1_home import views
urlpatterns = [
    re_path(r'^$', views.welcome, name='welcome'),
    #re_path(r'^app1_home', include('app1_home.urls')),
]