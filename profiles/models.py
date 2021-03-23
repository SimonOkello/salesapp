from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user =OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='No Bio')
    avatar = models.ImageField(upload_to='profiles', default='default.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username