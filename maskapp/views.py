from datetime import datetime
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import order,mask,admins,order, users

# Create your views here.
def login_view(request):
    return render(request,'index.html') 

def register(request):
    return render(request,'register.html') 

def addmask(request):
    return render(request,'addmask.html') 

def base(request):
    return render(request,'base.html') 

def base1(request):
    return render(request,'base1.html') 

def maskrequest(request):
    results1 = mask.objects.all()
    return render(request,'maskrequest.html',{"showmask":results1})

def showrequests(request):
    results1 = order.objects.all()
    return render(request,'showrequests.html',{"showreq":results1})

def profile(request):
    user = val()
    results = users.objects.filter(name = user)
    return render(request,'profile.html',{"showprof":results})

def myrequests(request):
    user = val()
    results = order.objects.filter(user = user)
    return render(request,'myrequests.html',{"showreq":results})



def login(request):
    if request.method == 'POST':
        uid = request.POST['username']
        upass = request.POST['password']
        global val
        def val():
            return uid
        if users.objects.filter(name = uid,password = upass,key = "u").exists():
            return redirect('base1')
        elif admins.objects.filter(username = uid,password = upass,key = "a").exists():
            return redirect('base')
        else :
            return HttpResponse("Invalid Credentials")
    else :
        return HttpResponse("Error")
    


def reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        gmail = request.POST['gmail']
        gender = request.POST['gender']
        password = request.POST['password']
        key = "u"
        new_user = users(name = name,gmail = gmail,gender = gender,password = password,key = key)
        new_user.save()
        return HttpResponse('Added')
    elif request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse("Not Added")
    
    
def newmask(request):
    if request.method == 'POST':
        type = request.POST['type']
        rate = request.POST['rate']
        qty = request.POST['qty']
        new_mask = mask(type = type,rate = rate,qty = qty)
        new_mask.save()
        messages.add_message(request,messages.ERROR,"Added Successfully")
        return render(request, 'addmask.html')
    elif request.method == 'GET':
        return render(request, 'addmask.html')
    else:
        return HttpResponse("Not Added")
    
def makerequest(request):
    if request.method == 'POST':
        user = val()
        type = request.POST['type']
        qty = request.POST['qty']
        date = datetime.now()
        if type == "" or qty == "":
            messages.add_message(request,messages.ERROR,"Pls Fill All Data")
        else:
            newreq = order(user = user,type = type,qty = qty,date = date)
            newreq.save()
            messages.add_message(request,messages.ERROR,"Order placed")
            return render(request, 'maskrequest.html')
    elif request.method == 'GET':
        return render(request, 'maskrequest.html')
    else:
        messages.add_message(request,messages.ERROR,"Error")
        return render(request, 'maskrequest.html')
        