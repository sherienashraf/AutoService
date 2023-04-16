from django.shortcuts import render , redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


from .models import Client
# Create your views here.

def signup_request(request):
    if request.method == "POST": 
        if request.POST['password1'] == request.POST['password2']:
            try:
                Client.objects.get(username=request.POST['username'])
                return render (request,'accounts/signup.html', {'error':'Sorry, Username is already Used, please enter another username'})
            except Client.DoesNotExist:
                client = Client.objects.create(
                    username=request.POST.get('username'),
                    email=request.POST.get('email'),
                    password=make_password(request.POST.get('password1')),
                    phone = request.POST.get('phone'),
                    government = request.POST.get('government'),
                    regon = request.POST.get('regon'),
                    car_name = request.POST.get('cname'),
                    car_model=request.POST.get('cmodel'),
                )
                client.save()   
                auth.login(request,client)
                return redirect('home')
        else:
            return render (request,'accounts/signup.html', {'error':'Sorry, Password does not match'})
    else:
        return render(request,'accounts/signup.html')



def login_request(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')         
        else:
            return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'accounts/login.html')

@login_required
def logout_request(request):
    auth.logout(request)
    return redirect('home')