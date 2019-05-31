from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
     return render(request, "eBaseManage.html")


def index(request):
    return render(request, "index.html")
