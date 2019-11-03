from django.shortcuts import render
from django.http import HttpResponse

def cookieCrumbs(request):
    return render(request, 'cookiecrumbsapp/cookieCrumbs.html')

def getTrail(request):
    return HttpResponse("getTrail")

def cookieTrail(request):
    return render(request, 'cookiecrumbsapp/cookieTrail.html')