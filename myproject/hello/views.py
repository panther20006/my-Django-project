from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def Homepageview(request):
    return render(request, "homepage.html")
def Aboutpageview(request):
    return render(request, "About.html")
def Contactpageview(request):
    return render(request, "contact.html")

def formpageprocess(request):
    return render(request, "form.html")

def ansprocess(request):
  a = int(request.POST["txt1"])
  b = int(request.POST["txt2"])
  c = a + b
  return render(request,'ans.html',{'mya':a,'myb':b,'myc':c})
  #return render(request,"ans.html", {'mya': a, 'myb': b, 'sum': c})

def ansprocess(request):
    return render("ANSPROCESS IS WORKING")

def savesessiondata(request):
    request.session["username"] = "Het soni"
    return HttpResponse("Session created")

def getsessiondata(request):
    if request.session.get("username"):
        msg = request.session.get('username')
        return HttpResponse('Username is ' + msg)
    else:
        return HttpResponse("No session data found")

def delsessiondata(request):
    del request.session["username"]
    return HttpResponse("Session data deleted")

def getsesionDate2 (request):
    if request.session.get("username"):
        msg = request.session.get('username')
        return HttpResponse( msg)
    else:
        return HttpResponse("No session data found")

def loginpageview(request):
    return render(request, "login.html")

def loginprocess(request):
    txt1=request.POST['email']
    request.session['myemail']=txt1
    return redirect(dashboard)

def dashboard(request):
    if 'myemail' in request.session:
        return render(request, 'dashboard.html')
    else:
        return redirect(loginpageview)

def logout(request):
    del request.session['myemail']
    return redirect(loginpageview)