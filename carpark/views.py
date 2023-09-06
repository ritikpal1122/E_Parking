from django.shortcuts import render,redirect,HttpResponse
from parking.models import ParkingInfo,ParkingLocation,ParkingSpace,BookSpace
from signup.models import Signup
def home(request):
    if "em" in request.session:
        uid=request.session['em']
        usr=Signup.objects.filter(id=uid)
        status="login"
        un="Welcome:"+str(usr[0].Name)
        status="logout"
    else:
         un="Welcome:Guest"
         status="login"    
    ob=ParkingLocation.objects.all()
    return render(request,"home.html",{'dt':ob,"name":un,"login":status})
def about(request):
    if "em" in request.session:
        uid=request.session['em']
        usr=Signup.objects.filter(id=uid)
        status="login"
        un="Welcome:"+str(usr[0].Name)
        status="logout"
    else:
         un="Welcome:Guest"
         status="login"    
    return render(request,"about.html",{"name":un,"login":status})
def contact(request):
    if "em" in request.session:
        uid=request.session['em']
        usr=Signup.objects.filter(id=uid)
        status="login"
        un="Welcome:"+str(usr[0].Name)
        status="logout"
    else:
         un="Welcome:Guest"
         status="login"    
    return render(request,"contact.html",{"name":un,"login":status})
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")
def logout(request):
    del request.session['em']
    return redirect(home)
def viewparking(request):
    if "em" in request.session:
        uid=request.session['em']
        usr=Signup.objects.filter(id=uid)
        status="login"
        un="Welcome:"+str(usr[0].Name)
        status="logout"
    else:
         un="Welcome:Guest"
         status="login"    
    ob=ParkingLocation.objects.all()
    return render(request,"viewparking.html",{"name":un,"login":status,'ob':ob})
def parkbyloc(request):
    id=request.POST["lid"]
    ob1=ParkingInfo.objects.filter(id=id)
    return render(request,"ajax/getpark.html",{'ob':ob1})
def parkbyloc1(request):
    id=request.POST["lid"]
    ob1=ParkingInfo.objects.filter(id=id)
    return render(request,"ajax/getparkcombo.html",{'ob':ob1})
def viewspace(request):
    id=request.POST["pid"]
    ob1=ParkingSpace.objects.filter(ParkingID=id)
    return render(request,"ajax/getspace.html",{'ob':ob1})
def viewspace1(request):
    id=request.POST["pid"]
    ob1=ParkingSpace.objects.filter(ParkingID=id)
    return render(request,"ajax/getspacecombo.html",{'ob':ob1})
def bookspace(request,bid):
    if "em" in request.session:
        uid=request.session['em']
        usr=Signup.objects.filter(id=uid)
        status="login"
        un="Welcome:"+str(usr[0].Name)
        status="logout"
    else:
         un="Welcome:Guest"
         status="login"
    ob1=ParkingSpace.objects.raw("select ps.id,ps.SpaceName,ps.Description,ps.Status,p.ParkingName from parkinginfo p,parkingspace ps where p.id=ps.ParkingID_id and ps.id="+str(bid))
    return render(request,"bookspace.html",{"name":un,"login":status,'pname':ob1[0].ParkingName,'spname':ob1[0].SpaceName,"desc":ob1[0].Description,'spid':ob1[0].id})
def booknow(request):
    
    if "em" in request.session:
        name=request.POST["name"]
        mobile=request.POST["mobile"]
        bdate=request.POST["bdate"]
        btime=request.POST["btime"]
        pmode=request.POST["pmode"]
        cholder=request.POST["cholder"]
        cardno=request.POST["cardno"]
        cvv=request.POST["cvv"]
        spid=request.POST["spid"]
        bby=request.session['em']
        ob1=BookSpace(Name=name,Mobile=mobile,BookDate=bdate,BookTime=btime,PaymentMode=pmode,CardHolderName=cholder,CardNo=cardno,CVV=cvv,Status="Booked",bookedby_id=bby,SpaceID_id=spid)
        ob1.save()
        member = ParkingSpace.objects.get(id=spid)
        member.Status = "Booked"
        member.save()
        if ob1:
            return HttpResponse("Booked")
        else:
            return HttpResponse("Cannot Book this time")
    else:
        return HttpResponse("Please Login First")
def mybooking(request):
    if "em" in request.session:
        uid=request.session['em']
        usr=Signup.objects.filter(id=uid)
        status="login"
        un="Welcome:"+str(usr[0].Name)
        status="logout"
    else:
         un="Welcome:Guest"
         status="login"    
    bby=request.session['em']
    ob1=ParkingSpace.objects.raw("select bs.*,ps.id,ps.SpaceName,ps.Description,ps.Status,p.ParkingName from parkinginfo p,parkingspace ps,bookspace bs where bs.SpaceID_id=ps.id and p.id=ps.ParkingID_id and bs.bookedby_id="+str(bby))
    return render(request,"mybooking.html",{'ob':ob1,"name":un,"login":status})
