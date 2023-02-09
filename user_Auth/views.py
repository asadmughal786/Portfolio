from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import user_register
from .froms import User_Login, User_registerations
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def user_login(request):
    if request.method == "POST":

        form = User_Login(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['login_email']
            password = form.cleaned_data['login_pass']
            user_data = user_register.registration.filter(user_email=email,user_password=password).first()
            if user_data:
                return HttpResponse("Successfully login!")
            else:
                messages.error(request,'Invalid Email or Password',extra_tags='danger')
    else:
        form = User_Login()
    return render(request,'login.html',{'form':form})

def Reg(request):
    if request.method == 'POST':
        form = User_registerations(data=request.POST,files=request.FILES)
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
            profile_image = form.cleaned_data['user_profile_picture']
            website_link = form.cleaned_data['user_website']
            password = make_password(form.cleaned_data['user_password'])
            checkPassword = check_password(form.cleaned_data['user_password'],password)

            print("---->Encrypted password: ",password)
            print("---->Decrypted Password: ",checkPassword)

            user_data = user_register.registration.filter(user_email=email,user_website = website_link).first()
            if not user_data:
                if checkPassword==True:
                    user = user_register(user_first_name=fname,user_last_name=lname,user_age=age,user_phone=phoneNumber,user_email=email,user_address=address,user_city=city,user_freelancer=is_freelancer,user_bio=bio,user_profile_picture=profile_image,user_website=website_link,user_password=password)
                    user.save()
                    messages.success(request,'User Registered Successfully!')
                else:
                    messages.error(request,"Password Doesn't matched!",extra_tags='danger')
                    form = User_registerations()
                return render(request,'registeration.html',{'form':form})
            else:
                messages.error(request,'Email or URL Already Exists! Please Try with another...',extra_tags='danger')
                form = User_registerations()
            return render(request,'registeration.html',{'form':form})
    else:
        form = User_registerations()
    return render(request,'registeration.html',{'form':form})