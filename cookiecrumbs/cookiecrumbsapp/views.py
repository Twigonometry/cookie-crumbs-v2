from django.shortcuts import render
from django.http import HttpResponse
import PyChromeDevTools as pyChrome
import http.cookies as cookies
import json

def cookieCrumbs(request):
    return render(request, 'cookiecrumbsapp/cookieCrumbs.html')

def getTrail(request):
    #setting up chrome dev tools interface
    chrome = pyChrome.ChromeInterface()
    chrome.Network.enable()
    chrome.Page.enable()

    #temporary call to google.com
    chrome.Page.navigate(url="https://www.google.com/")
    chrome.wait_event("Page.frameStoppedLoading",timeout=60)

    #get cookies
    cookies = chrome.Network.getCookies()

    #pass cookies back to cookieTrail
    newstr = " ".join(("http://127.0.0.1:8000/cookiecrumbsapp/cookieTrail?cookieList=", str(cookies)))
    chrome.Page.navigate(url=newstr)

    return HttpResponse("")

def cookieTrail(request):
    #get cookies from url header and turn into dictionary
    cookieList = request.GET.get('cookieList')
    cookieDump = eval(cookieList)

    #parse cookies as dictionary entries and save into array
    cookieObjects = []
    for cookie in cookieDump['result']['cookies']:
       cookieObjects.append(cookie)

    return render(request, 'cookiecrumbsapp/cookieTrail.html', {'cookieObjects':cookieObjects})