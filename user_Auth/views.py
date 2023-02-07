from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import user_register
from .froms import User_Login, User_registerations

# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = User_Login(data=request.POST)
        print("working")
        if form.is_valid():
            print("-----> Form Valid Done")
            email = form.cleaned_data['login_email']
            print('---> Email: ',email)
            password = form.cleaned_data['login_pass']
            print('---> Password: ',password)
            user_data = user_register.objects.filter(user_email=email,user_password=password).first()
            if user_data:
                return HttpResponse("Successfully login!")
            else:
                print("Invalid data")
                messages.error(request,'Invalid Email or Password')
    else:
        form = User_Login()
        print("--> get request")
    return render(request,'login.html',{'form':form})


def Reg(request):

    if request.method == 'POST':
        form = User_registerations(data=request.POST)
        if form.is_valid():
            print("Validation in View running!")
            fname = form.cleaned_data['user_first_name']
            lname = form.cleaned_data['user_last_name']
            age = form.cleaned_data['user_age']
            phoneNumber = form.cleaned_data['user_phone']
            email = form.cleaned_data['user_email']
            address = form.cleaned_data['user_address']     
            city = form.cleaned_data['user_city']
            is_freelancer = form.cleaned_data['user_freelancer']
            bio = form.cleaned_data['user_bio']
            # profile_image = form.cleaned_data['user_profile_picture']
            website_link = form.cleaned_data['user_website']
            password = form.cleaned_data['user_password']
            conf_password = form.cleaned_data['user_conf_password']
            user_data = user_register.objects.filter(user_email=email)
            if user_data:
                if password == conf_password:
                    user = user_register(user_first_name=fname,user_last_name=lname,user_age=age,user_phone=phoneNumber,user_email=email,user_address=address,user_city=city,user_freelancer=is_freelancer,user_bio=bio,user_webstie=website_link,user_password=password,user_conf_password=conf_password)
                    user.save()
                    messages.success(request,'User Registered Successfully!')
                else:
                    messages.error(request,"Password Doesn't matched!")
                    form = User_registerations()
                return render(request,'registeration.html',{'form':form})
    else:
        form = User_registerations()
    return render(request,'registeration.html',{'form':form})