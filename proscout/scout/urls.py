
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    url('homepage', views.index),

]