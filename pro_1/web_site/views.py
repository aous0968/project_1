from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .forms import RegisterForm , CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    authentication_form = CustomAuthenticationForm

@login_required(redirect_field_name="login")
def home(request, *args, **kwargs):
    context = {}

    return render(request, "home.html", context)

def register(request , *args, **kwargs):
    if request.POST : 
        pass
    form = RegisterForm()
    context = {'form' : form}
    return render(request , "registration/register.html" , context)