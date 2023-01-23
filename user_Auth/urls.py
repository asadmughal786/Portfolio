from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login,name='login'),
    path('registeration/',views.Registerations,name='regitseration'),
    path('reg/',views.Reg,name='reg'),
]
