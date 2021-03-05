from django.shortcuts import render, resolve_url, get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from .forms import SignupForm

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/user_form.html'
    success_url = settings.LOGIN_URL

class LoginView(LoginView):
    template_name = 'accounts/user_form.html'

class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        object = get_object_or_404(get_user_model(), username=self.kwargs['username'])
        return object