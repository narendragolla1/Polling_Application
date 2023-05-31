from django.shortcuts import render,HttpResponse
from django.contrib.auth.views import(
LoginView as Login ,
LogoutView as Logout
)
# Create your views here.
class login(Login):
    template_name='app/login.html'
    allow_auth_user=False
    
class logout(Logout):
    template_name='app/logout.html'
    
    