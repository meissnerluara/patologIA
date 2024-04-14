from django.urls import path
from . import views

app_name = 'AccountsApp'

urlpatterns = [
    path('UserSignUp/', views.ViewSignUp, name='SignUpView'),
    path('UserLogIn/', views.ViewLogIn, name='LogInView'),
    path('UserLogOut/', views.ViewLogOut, name='LogOutView'),
]
