from django.db import models

# Create your models here.


from django.conf import settings
from django.utils import timezone

class FriendList(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        
        if not account in self.friends.all():
            self.friends.add(account)
            self.save()
        




