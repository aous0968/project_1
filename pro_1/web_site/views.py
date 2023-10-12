from .forms import RegisterForm, CustomAuthenticationForm

from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
# Create your views here.


@login_required(login_url="My_login", redirect_field_name="")
def home(request, *args, **kwargs):
    context = {}

    return render(request, "home.html", context)


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('home')
    authentication_form = CustomAuthenticationForm


def register(request, *args, **kwargs):
    if request.user.is_authenticated :
        return redirect('home')
    form = RegisterForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            user_name = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            get_user_model().objects.create_user(username=user_name, email=email,
                                                 password=password, first_name=first_name, last_name=last_name)
            user = authenticate(username=user_name, password=password)
            login(request, user)
            return redirect("My_login")

    context = {'form': form}
    return render(request, "registration/register.html", context)
