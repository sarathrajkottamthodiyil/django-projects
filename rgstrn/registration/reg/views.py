from django.shortcuts import render
from.models import new_user
from hashlib import sha256
def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pincode=request.POST.get('pincode')
        phone=request.POST.get('phone')
        job=request.POST.get('job')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        password = sha256(pass2.encode()).hexdigest()
        new_user(username=username, email=email, pincode=pincode, phone_no=phone, job_type=job, password=password).save()




    return render(request, 'reg.html')