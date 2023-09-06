from django.shortcuts import render,HttpResponse
from signup.models import Signup
def saveaccount(request):
    email=request.POST["email"]
    name=request.POST["name"]
    mobile=request.POST["mobile"]
    psw=request.POST["psw"]
    username=request.POST["uname"]
    address=request.POST["address"]
    gender=request.POST["gender"]
    ob=Signup(Email=email,Name=name,Address=address,ContactNo=mobile,Password=psw,UserName=username,Gender=gender)
    ob.save()
    return HttpResponse("Record Saved")
def login(request):
    username=request.POST["uname"]
    password=request.POST["psw"]
    ob=Signup.objects.filter(UserName=username,Password=password)
    request.session['em']=ob[0].id
    if ob:
        return HttpResponse("Valid User")
    else:
        return HttpResponse("Invalid user")
