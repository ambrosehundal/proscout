from django.shortcuts import render
from django.http import HttpResponse
import json
from account.models import Account
from friend.models import FriendRequest


# Create your views here.

def send_friend_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    
    if request.method == "POST" and user.is_authenticated:
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            receiver = Account.objects.get(pk=user_id)
            try:
                # get any friend requests that are active
                friend_requests = FriendRequest.objects.filter(sender=user, receiver=receiver)
                
                #find if any of them are active
                try:
                    for request in friend_requests:
                        if request.is_active:
                            raise Exception("Friend Request has already been sent")

                    # if none are active, then create a nre friend request
                    friend_request = FriendRequest(sender=user, receiver=receiver)
                    friend_request.save()
                    payload['response'] = "Friend request created"
                except Exception as e:
                    payload['response'] = str(e)

            
            except FriendRequest.DoesNotExist:
                friend_request = FriendRequest(sender=user, receiver=receiver)
                friend_request.save()
                payload['response'] = "Friend request created"

            if payload['response'] = None:
                payload['response'] = "Something went wrong"
        
        else:
            payload['response'] = "Unable to send a friend request"
    else:
        payload['response'] = "You must be unathenticated to send a friend request"

    return HttpResponse(json.dumps(payload), content_type="application/json")
    
        
                



