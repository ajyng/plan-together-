from django.urls import path, include
from . import views

urlpatterns = [
    path('<username>/', views.ProfileView.as_view(), name='profile'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
]