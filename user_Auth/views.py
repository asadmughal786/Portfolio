from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import *
from .froms import *
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

# ---------------------------------------------------------Login View----------------------------------

def user_login(request):
    if request.method == "POST":

        form = User_Login(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['login_email']
            password = form.cleaned_data['login_pass']
            user_data = user_register.registration_obj.filter(user_email=email,user_password=password).first()
            if user_data:
                return HttpResponse("Successfully login!")
            else:
                messages.error(request,'Invalid Email or Password',extra_tags='danger')
    else:
        form = User_Login()
    return render(request,'login.html',{'form':form})

# -----------------------------------------------------Regitration View----------------------------------

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
            country = form.cleaned_data['user_country']
            is_freelancer = form.cleaned_data['user_freelancer']
            bio = form.cleaned_data['user_bio']
            profile_image = form.cleaned_data['profile_picture']
            website_link = form.cleaned_data['user_website']
            password = make_password(form.cleaned_data['user_password'])
            checkPassword = check_password(form.cleaned_data['user_password'],password)

            print("---->Encrypted password: ",password)
            print("---->Decrypted Password: ",checkPassword)

            user_data = user_register.registration_obj.filter(user_email=email,user_website = website_link).first()
            if not user_data:
                if checkPassword==True:
                    user = user_register(user_first_name=fname,user_last_name=lname,user_age=age,user_phone=phoneNumber,user_email=email,user_address=address,city=city,country=country,user_freelancer=is_freelancer,user_bio=bio,user_profile_picture=profile_image,user_website=website_link,user_password=password)
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

# --------------------------------------------------Profile View--------------------------------------

def user_profile(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = user_register.registration_obj.get(pk=id)
            skill_data = skills.Skill_obj.filter(user_skills=id).all()
            education_data = Education.education_obj.filter(user_education=id).all()
            professional_data = professional_experiance.prof_exp_obj.filter(user_company=id).all()
            
        else:
            form = profile()
        return render(request,'proifle.html',{'form':form,'user_data':data ,'user_skills': skill_data,'Education_data':education_data,'professional_data':professional_data})
    else:
        messages.error(request,'You are not Authorized to Access this Page',extra_tags="danger")
    return HttpResponseRedirect("/login/")

# ------------------------------------------------Add Skills View-------------------------


def add_skills(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = skills(request.POST)
            if form.is_valid():
                skill_name = form.cleaned_data['skill_name']
                skill_grip = form.cleaned_data['skill_grip_value']
                data = skills(skill_name=skill_name,grip_value=skill_grip, user_skills = id)
                data.save()
                messages.success(request,'Data saved successfully')
                skills_data = skills.Skill_obj.filter(user_skills = id).all()
            else:
                messages.error(request,'Invalid Data entered!',extra_tags='danger')
                form = skills()
            return render(request,'skills.html',{'form':form,'skills_data':skills})
        else:
            form = skills()
        return render(request,'skills.html',{'form':form,'skills_data':skills_data})
    else:
        messages.error('You are not Authorized to access this page!')
    return HttpResponseRedirect('/login/')

# -------------------------------------------------------------Add Education View-----------------------------

def add_education(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Education(request.POST)
            if form.is_valid():
                degree_name = form.cleaned_data['degree_name']
                degree_city = form.cleaned_data['degree_city']
                degree_country = form.cleaned_data['degree_country']
                degree_start_date = form.cleaned_data['degree_start_date']
                degree_end_date = form.cleaned_data['degree_end_date']
                data = Education(Name_of_degree=degree_name,city = degree_city,country=degree_country,start_date=degree_start_date,end_date=degree_end_date,user_education=id)
                data.save()
                education_data = Education.education_obj.filter(user_education=id).all()
                messages.success(request,'Education Information added successfully!')
            else:
                form = Education()
                messages.error(request,'Invalid form data',extra_tags='danger')
            return render(request,'education.html',{"form":form,'education_data':education_data})
        else:
            form = Education()
        return render(request,'education.html',{'form':form,'education_data':education_data})
    else:
        messages.error(request,'You are not Authorized to Access this page',extra_tags='danger')
    return HttpResponseRedirect("/login/")

# -----------------------------------------------Add Educational Achivement View----------------------------

def add_educ_achive(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = achivements(request.POST)
            if form.is_valid():
                achievement_title = form.cleaned_data['achievement_title']
                achievement_link = form.cleaned_data['achievement_link']
                certification_start_date = form.cleaned_data['certification_start_date']
                certification_end_date = form.cleaned_data['certification_end_date']
                achive_data = professionl_achivements(achivements_name = achievement_title,certification_link=achievement_link,certification_start_date=certification_start_date,certification_end_date=certification_end_date)
                achive_data.save()
                data = Educative_achivements.edu_achivements_obj.filter(education=id).all()
            else: 
                messages.error(request,'invalid form data',extra_tags='danger')
            return render(request,'edu_achivement.html',{'form':form,'achive_data':data})
        else:
            form = achivements()
        return render(request,'achivement.html',{'form':form,'achive_data':data})
    else:
        messages.error(request,'You are not Authorized to access this page',extra_tags='danger')
    return HttpResponseRedirect('/login/')
            

# -----------------------------------------------Add Professional experience View----------------------

def add_profExp(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfessionalExp(request.POST)
            if form.is_valid():
                company_name = form.cleaned_data['company_name']
                city = form.cleaned_data['company_city']
                country = form.cleaned_data['company_country']
                job_start_date = form.cleaned_data['job_start_date']
                job_end_date = form.cleaned_data['job_end_date']
                data = professional_experiance(user_company = company_name,start_date=job_start_date,end_date=job_end_date,city = city, country=country)
                data.save()
                prof_data = professional_experiance.prof_exp_obj.filter(user_company=id).all()
            else:
                messages.error(request,'Invalid form data',extra_tags= 'danger')
            return render(request,'skills.html',{'form':form,'prof_data':prof_data})
        else:
            form = ProfessionalExp()
        return render(request,'skills.html',{'form':form})
    else:
        messages.error(request,'You are not Authorized to access this page',extra_tags='danger')
    return HttpResponseRedirect('/login/')

# -------------------------------------------------------Add Professional achivements View--------------------------

def add_prof_achive(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = achivements(request.POST)
            if form.is_valid():
                achievement_title = form.cleaned_data['achievement_title']
                achievement_link = form.cleaned_data['achievement_link']
                certification_start_date = form.cleaned_data['certification_start_date']
                certification_end_date = form.cleaned_data['certification_end_date']
                achive_data = professionl_achivements(achivements_name = achievement_title,certification_link=achievement_link,certification_start_date=certification_start_date,certification_end_date=certification_end_date)
                achive_data.save()
                data = professionl_achivements.p_achievements_obj.filter(p_achievement=id)
            else: 
                messages.error(request,'invalid form data',extra_tags='danger')
            return render(request,'achivement.html',{'form':form,'achive_data':data})
        else:
            form = achivements()
        return render(request,'achivement.html',{'form':form,'achive_data':data})
    else:
        messages.error(request,'You are not Authorized to access this page',extra_tags='danger')
    return HttpResponseRedirect('/login/')
            




