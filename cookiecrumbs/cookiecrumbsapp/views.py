from django.shortcuts import render
from django.http import HttpResponse

def cookieCrumbs(request):
    return HttpResponse("cookieCrumbs")

def getTrail(request):
    return HttpResponse("getTrail")

def cookieTrail(request):
    return HttpResponse("cookieTrail")