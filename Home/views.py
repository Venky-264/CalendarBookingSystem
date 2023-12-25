from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.views.decorators.cache import cache_control

# Create your views here.

def HomePage(request):
    return render(request,'Home/index.html')

def LoginPage(request):
    return render(request,'Home/login.html')  
def Register(request):
    if request.method == 'POST':
        usermail=request.POST['mail']
        userphone=request.POST['phone']
        username=request.POST['name']
        userpassword=request.POST['password']
        flag=Students.objects.filter(email=usermail).count()
        if(flag!=1):
            id=Students.objects.all().count()+1
            Students(id,usermail,userphone,username,userpassword).save()
            url='/user/{}'.format(usermail)
            return redirect(url)
        else:
            messages.error(request, 'User already exist')
            return redirect('/')
def User(request,user):
    flag=Students.objects.filter(email=user).count()
    if(flag==1):
        courses=Courses.objects.all()
        return render(request,'Home/user.html',{'c':courses})
    else:
        return render(request,'Home/404.html')

def Lecturer(request,lecturer):
    flag=Lecturers.objects.filter(email=lecturer).count()
    if(flag==1):
        bookedcourses=Booked.objects.all()
        return render(request,'Home/lecturer.html',{'courses':bookedcourses})
    else:
        return render(request,'Home/404.html')

def admin(request,admin):
    flag=Admin.objects.filter(email=admin).count()
    if(flag==1):
        return render(request,'Home/admin.html')
    else:
        return render(request,'Home/404.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def validate(request):
    if request.method=='POST':
        usertype=request.POST['type']
        usermail=request.POST['mail']
        userpassword=request.POST['password']

        if(usertype=='Student'):
            flag=Students.objects.filter(email=usermail,password=userpassword).count()
            if(flag==1):
                url='/user/{}'.format(usermail)
                return redirect(url)
            else:
                messages.error(request, 'invalid credentials')
                return redirect('/login')
        if(usertype=='Lecturer'):
            flag=Lecturers.objects.filter(email=usermail,password=userpassword).count()
            if(flag==1):
                url='/lecturer/{}'.format(usermail)
                return redirect(url)
            else:
                messages.error(request, 'invalid credentials')
                return redirect('/login')
        if(usertype=='Admin'):
            flag=Admin.objects.filter(email=usermail,password=userpassword).count()
            if(flag==1):
                url='/useradmin/{}'.format(usermail)
                return redirect(url)
            else:
                messages.error(request, 'invalid credentials')
                return redirect('/login')

def addcourse(request):
    if request.method=='POST':
        cname=request.POST['name']
        level=request.POST['level']
        id=Courses.objects.all().count()+1
        Courses(id,cname,level).save()
        return redirect('/login')
     
def logout(request):
    return redirect('/login')

def addtutor(request):
    if request.method=='POST':
        usermail=request.POST['mail']
        userphone=request.POST['phone']
        username=request.POST['name']
        userpassword=request.POST['password']
        flag=Lecturers.objects.filter(email=usermail).count()
        id=Lecturers.objects.all().count()+1
        Lecturers(id,usermail,userphone,username,userpassword).save()
        return redirect('/login')
def deletetutor(request):
    if request.method=='POST':
        usermail=request.POST['mail']
        Lecturers.objects.filter(email=usermail).delete()
        return redirect('/login')
def Bookslot(request):
    if request.method=='POST':
        usermail=request.POST['mail']
        level=request.POST['level']
        cname=request.POST['cname']
        date=request.POST['date']
        id=Booked.objects.all().count()+1
        booked=Booked(id,usermail,cname,level,date).save()
        return redirect('/login')