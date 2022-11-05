import email
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']
    
    newuser=Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)
    return redirect("show")

def ShowData(request):
    alldata=Student.objects.all()
    return render(request,"app/show.html",{'key':alldata})

