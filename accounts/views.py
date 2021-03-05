from django.shortcuts import render, resolve_url
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import SignupForm

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/user_form.html'
    success_url = settings.LOGIN_URL

class LoginView(LoginView):
    template_name = 'accounts/user_form.html'

def profile(request):
    pass