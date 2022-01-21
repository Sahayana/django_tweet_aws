from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"    # give a specific table name to DB.

    
    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee', blank=True)