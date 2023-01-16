from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .froms import *

# Create your views here.

def Registerations(request):
    
    if request.method == 'POST':
        form = User_registerations(request.POST,request.FILES)
        if form.is_valid():
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
            password = form.cleaned_data['user_password']
            conf_password = form.cleaned_data['user_conf_password']
            if password == conf_password:
                user = user_resgisteration(user_first_name=fname,user_last_name=lname,user_age=age,user_phone=phoneNumber,user_email=email,user_address=address,user_city=city,user_freelancer=is_freelancer,user_bio=bio,user_profile_picture=profile_image,user_webstie=website_link,user_password=password,user_conf_password=conf_password)
                user.save()
                messages.success(request,'User Registered Successfully!')
            else:
                messages.error(request,"Password Doesn't matched!")
                form = User_registerations()
            return render(request,'registeration.html',{'form':form})
            return HttpResponse("Working")
        # return HttpResponseRedirect('/')
        return HttpResponse("outer Working")
    # return render(request,'registeration.html',{"form":form})
    else:
        form = User_registerations()
    return render(request,'registeration.html',{'form':form})


def login(request):
    return render(request,"login.html")