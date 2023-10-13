"""
URL configuration for Pro_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from pro_1 import settings
# from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from web_site.views import (
    home,
    register,
    username_validation,
    MyLoginView,
    ResetPasswordView,
)


urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", MyLoginView.as_view(), name="My_login"),
    path("login/username-validation/", username_validation , name="username_validation"),
    path("logout/", auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
    path("password-reset/", ResetPasswordView.as_view(), name="password_reset"),
    path("password-reset-confirm/<uidb64>/<token>/",  auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/reset/password_reset_complete.html'),
         name='password_reset_complete'),
]
