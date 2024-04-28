from django.db import models

# Create your models here.

from django.utils import timezone

class user(models.Model):
    
    name =  models.CharField(max_length=100)
    profile_pic =  models.ImageField(upload_to ='profiles/',default='',blank=True)
    password =  models.CharField(max_length=100)
    about = models.TextField(default='~')


class friends(models.Model):

    current_user = models.ForeignKey(user,related_name='user',on_delete=models.CASCADE)

    friend =  models.ForeignKey(user,related_name='friends',on_delete=models.CASCADE)


class messages(models.Model):

    sender = models.ForeignKey(user,related_name='sender',on_delete=models.CASCADE)
    receiver =  models.ForeignKey(user,related_name='receiver',on_delete=models.CASCADE)
    message =  models.TextField()
    created_at = models.DateTimeField(default=timezone.now)



class ChatRoom(models.Model):

    sender = models.ForeignKey(user,related_name='sendingperson',on_delete=models.CASCADE)
    receiver =  models.ForeignKey(user,related_name='receivingperson',on_delete=models.CASCADE)
    message =  models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class BlockUser(models.Model):
    blocking_user =  models.ForeignKey(user,related_name='blocking_user',on_delete=models.CASCADE)
    blocked_user =  models.ForeignKey(user,related_name='blocked_user',on_delete=models.CASCADE)

