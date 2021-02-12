"""proscout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import re_path
from django.contrib import admin
from django.conf.urls import include
from registration import views as v
from scout import views as s
from friend import views



urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url('admin/', admin.site.urls),
    url('home/', include('scout.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url('accounts/password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html')),
    url('friend/', include('friend.urls', namespace='friend')),
    url('register/', v.register, name="register"),
    re_path(r'^$', s.index, name="index"),
    url('', include('social_django.urls', namespace='social'))
  
    
   



]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
