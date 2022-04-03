from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(type(request))
    return HttpResponse('Hello World!')
