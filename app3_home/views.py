from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hassan(Request):
    return HttpResponse("<a href='http://127.0.0.1:8000/app1_home'>Enter here for registration</a> <br> <a href='http://127.0.0.1:8000/app2_home'>Enter here for further information</a> <br> <h1>Hasan is best place</h1>")