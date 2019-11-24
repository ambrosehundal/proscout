
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    url('', views.index, name='homepage'),
    url('profile', views.profile_homepage, name='profile')


]