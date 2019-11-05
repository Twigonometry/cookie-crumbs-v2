from django.shortcuts import redirect
from django.http import HttpResponse
import sys;

def handler404(request, exception):
    # make a redirect to homepage
    return redirect('cookiecrumbsapp/cookieCrumbs')

def handler500(request):
    #handle error messages for debugging - set to obscure error once tested
    errType, errValue, errTraceback = sys.exc_info()
    return HttpResponse("500 internal server error\nError type: " + str(errType) + "\nError value: " + str(errValue) + "\nError traceback:\n", errTraceback)