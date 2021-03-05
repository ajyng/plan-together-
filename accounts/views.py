from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, DetailView
from .forms import SignupForm

User = get_user_model()

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/user_form.html'
    success_url = settings.LOGIN_URL

class ProfileView(DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)