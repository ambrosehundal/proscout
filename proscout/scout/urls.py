from django.urls import path, re_path
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView
from . import views
from scout.api import ProfileView


urlpatterns = [
    url('index', views.index, name='homepage'),
    re_path('profile/(?P<username>.+)/$', ProfileView.as_view(), name='edit_profile'),
    # url('profile/<str:username>/', views.profile_homepage, name='profile'),
    url('profile/new', views.new_profile, name='create_new_profile'),
    url('news', views.mma_subreddit, name='mma_news'),
    url('ufc', views.ufc_subreddit, name='ufc')
    


]
