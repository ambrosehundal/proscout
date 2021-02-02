
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView
from . import views



urlpatterns = [
    url('index', views.index, name='homepage'),
    url('profile', views.profile_homepage, name='profile'),
    url('create', views.new_profile, name='create_new_profile'),
    url('news', views.mma_subreddit, name='mma_news'),
    url('ufc', views.ufc_subreddit, name='ufc')
    


]
