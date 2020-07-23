from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from body.models import Profile,Trainer,Member,Session,Workout
# Create your views here.

def home(request):
    return render(request,'Home.html')

def contact(request):
    return render(request,'Contact.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']

        exists = User.objects.filter(username=username).exists()

        if not exists:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request,user)

            profile = Profile.objects.create(name=name,phone=phone,user=user, user_type=int(user_type))
            
            user_type = user.profile.user_type
            if user_type == 1:
                return redirect("/memberDashboard")
            else:
                 return redirect("/trainerDashboard")

    return render(request,'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            user_type = user.profile.user_type
            if user_type == 1:
                return redirect("/mprofile")
            else:
                 return redirect("/tprofile")
                
        else:
            return redirect("/signup")
    return render(request,"signin.html")

def signout(request):
    logout(request)
    return redirect("/")

def membership(request):
    return render(request,"membership.html")

def memberDashboard(request):
    member = Member.objects.filter(member=request.user)
    if request.method =="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        age = request.POST['age']
        gender = request.POST['gender']
        height = request.POST['height']
        weight = request.POST['weight']
        member = Member.objects.create(
            name= name,
            phone = phone,
            age = age,
            gender = gender,
            height = height,
            weight = weight,
            member = request.user
        )
        return redirect("/mprofile/")
    return render(request,"MemberDash.html")

def  trainerDashboard(request):
    if request.method =="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        age = request.POST['age']
        gender = request.POST['gender']
        experience = request.POST['experience']
        skills = request.POST['skills']
        trainer = Trainer.objects.create(
            name= name,
            phone = phone,
            age = age,
            gender = gender,
            experience = experience,
            skills = skills,
            trainer = request.user
        )
        return redirect("/tprofile/")    
    return render(request,"TrainerDash.html")

def mclass(request):
    classes=Workout.objects.all()
    return render(request,"mclass.html",{"classes":classes})

def tclass(request):
    if request.method =="POST":
        name = request.POST['name']
        date = request.POST['date']
        time = request.POST['time']
        duration = request.POST['duration']
        trainer = Trainer.objects.get(trainer=request.user)
        name = int(name)
        work = Workout.objects.get(pk=name)
        print(work)
        create_class = Session.objects.create(
        name = work,
        date = date,
        time = time,
        duration = duration,
        trainer= trainer,
        )
        print(create_class.pk)
        return redirect("/tclass/")
    return render(request,"tclass.html")

def mtrainer(request):
    trainers = Trainer.objects.all()
    return render(request,"mtrainer.html",{"trainers":trainers})

def ttrainee(request):
    trainer = Trainer.objects.get(trainer=request.user)
    members = Session.objects.filter(trainer=trainer)
    return render(request,"ttrainee.html",{"members":members})

def details(request,pk):
    work = Workout.objects.get(pk=pk)
    print(work)
    session = Session.objects.get(name=work)
    print(session.date)
    return render(request,"details.html",{"session":session})

def tprofile(request):
    print(request.user)
    trainer = Trainer.objects.get(trainer=request.user)
    return render(request,"tprofile.html",{"trainer":trainer})

def mprofile(request):
    member = Member.objects.get(member=request.user)
    return render(request,"mprofile.html",{"member":member})

def allclass(request):
    trainer = Trainer.objects.get(trainer=request.user)
    sessions = Session.objects.filter(trainer=trainer)
    return render(request,"allclass.html",{"sessions":sessions})

def subscribe(request,pk):
    if request.method =="POST":
        details = Session.objects.get(pk=pk)
        member = Member.objects.get(member=request.user)
        details.member = member
        details.save()
        return redirect("/mclass/")
    return render("/subscribe/",{"details":details})

def edit(request,pk):
    session = Session.objects.get(pk=pk)
    # print(session.name)
    if request.method =="POST":
        session = Session.objects.get(pk=pk)
        print(session)
        date = request.POST['date']
        time = request.POST['time']
        duration = request.POST['duration']
        trainer = Trainer.objects.get(trainer=request.user)
        session.date=date
        session.time=time
        session.duration=duration
        session.save()
        return redirect("/allclass/")
    return render(request,"edit.html",{"session":session})

def delete(request,pk):
     session = Session.objects.get(pk=pk)
     session.delete()
     return redirect("/allclass/")

def msession(request):
    member = Member.objects.get(member=request.user)
    print(member)
    sessions = Session.objects.filter(member=member)
    print(sessions)
    return render(request,"msession.html",{"sessions":sessions})
