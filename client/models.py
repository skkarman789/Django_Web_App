from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import  CustomUserManager

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True,blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

    def __str__(self):
        return self.first_name  + " " + self.last_name

class UserTask(models.Model):

    CHOIISES=(("Pending","Pending"),("Completed", "Completed"))
    user=models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name=("user"))
    title=models.TextField()
    description=models.TextField()
    status=models.CharField(max_length=15, choices=CHOIISES)
    date=models.DateField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title