from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("<h1>liz开发的后台网页</h1>")
    return render(request, 'index.html')

