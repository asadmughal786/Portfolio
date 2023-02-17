from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.user_login,name='user_login'),
    path('reg/',views.Reg,name='reg'),
    path('addSkills/<int:id>/',views.add_skills,name= 'add_skills'),
]
