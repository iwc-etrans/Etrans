from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    #return HttpResponse("Hello world ! ")
    # context = {}
    # context['hello'] = 'Hello World!'
     return render(request, "eBaseManage.html")
