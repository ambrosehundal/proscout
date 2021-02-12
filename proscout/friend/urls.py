from django.conf.urls import url

from friend import views


app_name = "friend"


urlpatterns = [
    url('friend_request/', views.send_friend_request, name='friend_request')
]
