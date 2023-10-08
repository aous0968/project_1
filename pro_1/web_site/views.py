from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
# Create your views here.


def home(request, *args, **kwargs):
    context = {}

    if not request.user.is_authenticated :
        return redirect("login")


    return render(request, "home.html", context)

def register(request , *args, **kwargs):
    if request.POST : 
        pass
    form = RegisterForm()
    context = {'form' : form}
    return render(request , "registration/register.html" , context)