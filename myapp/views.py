from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hello, world. My first project")


def index2(request, name):
    return HttpResponse(f'Hello, {name}')