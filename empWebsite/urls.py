from django.urls import path
from . import views

urlpatterns = [
    path("", views.projectEmporium, name='home'),
    path("login/", views.showLogin, name='login'),
    path("breakout/", views.showBreakout, name='breakout')
]