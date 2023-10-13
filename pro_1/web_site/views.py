from .forms import RegisterForm, CustomAuthenticationForm

from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView , PasswordResetView
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin

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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/reset/password_reset.html'
    email_template_name = 'registration/reset/password_reset_email.html'
    subject_template_name = 'registration/reset/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')


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
