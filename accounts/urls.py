from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name = 'accounts/user_form.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    re_path(r'^(?P<username>[\w.@+-]+)/$', views.ProfileView.as_view(), name='profile'),
]