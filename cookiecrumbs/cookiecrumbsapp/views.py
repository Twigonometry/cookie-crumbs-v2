from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
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

    #gets target url and visits it
    target = request.GET.get('target')
    chrome.Page.navigate(url=target)
    chrome.wait_event("Page.frameStoppedLoading",timeout=60)

    #get cookies
    cookieList = chrome.Network.getCookies()

    #pass cookies back to cookieTrail
    newstr = " ".join(("http://127.0.0.1:8000/cookiecrumbsapp/cookieTrail?cookieList=", str(cookieList)))
    chrome.Page.navigate(url=newstr)

    return HttpResponse("")

    #have the following in another view - returns cookies and target url in a nicer format (either as a cookie or param)
    #this will allow us to display url as a h3 element under "this is your cookie trail"
    #return redirect('cookiecrumbsapp/cookieTrail', {'cookieList':cookieList, 'target':target})

def cookieTrail(request):
    #get cookies from url header and turn into dictionary
    cookieList = request.GET.get('cookieList')
    cookieDump = eval(cookieList)

    #parse cookies as dictionary entries and save into array
    cookieObjects = []
    for cookie in cookieDump['result']['cookies']:
       cookieObjects.append(cookie)

    #generating stats about cookies
    insecureTotal = 0
    sessionTotal = 0

    for cookie in cookieObjects:
        if cookie['secure'] == False:
            insecureTotal+=1
        if cookie['session'] == True:
            sessionTotal+=1

    #try figuring out what type the variable 'cookie' is - error message = Error value: 'dict' object has no attribute 'secure'
    #try inside view, commenting out code above and replicating it there

    return render(request, 'cookiecrumbsapp/cookieTrail.html', {'cookieObjects':cookieObjects, 'insecureTotal':insecureTotal, 'sessionTotal':sessionTotal})