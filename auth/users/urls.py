from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    #path('user', UserView.as_view()),
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.login, name='login'),
]