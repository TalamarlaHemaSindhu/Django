from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,'home.html')

def loginView(request):
    if request.method=='POST':
        usern=request.POST.get('uname')
        pas=request.POST.get('passw')
        print(usern,pas)
        result=authenticate(request,username=usern,password=pas)
        if result is not None:
            login(request,result)
            if request.user.is_superuser:
               return redirect('/admin')
            else:
               return redirect('loginpage')    
    return render(request,'login.html')


@login_required(login_url='loginpage')
def profile(request):
    return render(request,'profile.html')

def register(request):
    if request.user.is_authenticated:
        messages.warning(request,"Man you already have an account !")
        return redirect('homepage')
        
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        passw=request.POST.get('passw')
        cpass=request.POST.get('cpass')
        email=request.POST.get('mail')
        uname=request.POST.get('uname')
        print(fname,lname,passw,cpass,email,uname)

        #validation username
        if User.objects.filter(username=uname).exists():
            messages.error(request,"Username already exists !")
            return redirect('loginpage')
        #validation for password
        if len(passw)<8:
            messages.error(request,"Password must be 8 chars")
            return redirect('registerpage')
        #validation for cpass
        if (cpass!=passw):
            messages.error(request,"Passwords doest match")
            return redirect('registerpage')
        
        obj=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=passw)
        obj.save()
        messages.success(request,"Hey your account is ready, Login now")
        return redirect('loginpage')

    return render(request,'register.html')




@login_required(login_url='loginpage')

def tweetView(request):
    if request.method=="POST":
        a=request.POST.get('post')
        u=str(request.user.username)
        obj=tweet(uname=u,post=a)
        obj.save()
    return render(request,'tweet.html')





def create(request):
    return render(request,'create.html')

def display(request):
    return render(request,'single.html')


def deleteView(request):
    return render(request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('loginpage')
    






    





