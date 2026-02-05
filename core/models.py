from django.db import models
from django.contrib.auth.models import AbstractUser
from django_extensions.db.fields import AutoSlugField


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to="profilepics/", null=True, blank=True)

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from=['name'], unique=True)   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content   
    

