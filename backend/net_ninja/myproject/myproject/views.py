# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
    # return HttpResponse("Hello Wrold!")

def about(request):
    # return HttpResponse("My About Page")
    return render(request,'about.html')
