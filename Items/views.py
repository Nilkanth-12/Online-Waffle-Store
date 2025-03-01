from django.shortcuts import render
from django.http import HttpResponse

def homes(request):
    return HttpResponse('<h1>Home</h1>')


