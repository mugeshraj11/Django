from django.shortcuts import render

# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")

def SignupPage(request):
    return render(request,"app/login.html")

