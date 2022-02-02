from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("The is the homepage for My Fin Hub Web APP.")

def quote(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "quote.html")

def summary(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "summary.html")




