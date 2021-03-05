from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import SignupForm

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup_form.html'
    success_url = settings.LOGIN_URL

def login(request):
    pass

def profile(request):
    pass