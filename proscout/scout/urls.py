
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from scout import views


urlpatterns = [
    url('homepage', views.index),
    
]