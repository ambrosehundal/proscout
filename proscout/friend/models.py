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


    def remove_friend(self, account):

        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):

        # remove both people from friends list
        remover_friends_list = self 

        remover_friends_list.remove_friend(removee)

        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)

    
    def is_mutual_friend(self, friend):

        if friend in self.friends.all():
            return True
        
        return False



# class FriendRequest(models.Model):

        





        




