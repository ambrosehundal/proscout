from django.shortcuts import render
from django.http import HttpResponse

import json

from account.models import account
from friend.models import FriendRequest


# Create your views here.

def send_friend_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    
    if request.method == "POST" and user.is_authenticated:
        receiver_id = request.POST.get("receiver_user_id")