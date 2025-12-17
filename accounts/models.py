from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser



class User(AbstractUser):

    ROLES=(
        ('ADMIN','admin'),
        ('MENTOR','mentor'),
        ('STUDENT','student')
    )
    role = models.CharField( max_length=10,choices=ROLES,default='student')

    def __str__(self):
        return self.username

