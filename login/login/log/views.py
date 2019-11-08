from django.shortcuts import render
from django.http import HttpResponse
from .models import Sign, Log, Save
# from django.http import HttpResponseRedirect
mail = []
pwd = []
def home(request):
    return render(request, 'home.html')
def sign(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("pwd")
    cpassword = request.POST.get("cpwd")
    Sign(username=username, email=email, password=password, conpassword=password).save()
    if password != cpassword:
        return render(request, 'home.html')
    if username == ' ' or email == ' ':
        return render(request, 'home.html')
    else:
        mail.append(email)
        pwd.append(password)
        return render(request, 'login.html')
def log(request):
    email = request.POST.get("email")
    password = request.POST.get("pwd")
    Log(email=email, password=password).save()
    if email in mail and password in pwd:
        return render(request, 'save.html')
    elif email == " " and password == " ":
        return HttpResponse("<html><body bgcolor='ORANGE'><h1>ENTER VALID EMAIL OR PASSWORD</h1></body></html>")
    else:
        return HttpResponse("<html><body bgcolor='ORANGE'><h1>ENTER VALID EMAIL OR PASSWORD</h1></body></html>")

def save(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    mobile = request.POST.get("mobile")
    address = request.POST.get("address")
    Save(name=name, email=email, mobile=mobile, address=address).save()
    return HttpResponse("<html><body bgcolor='ORANGE'><h1>saved successfully</h1></body></html>")
