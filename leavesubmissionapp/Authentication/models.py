from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

# Create your models here.
class AppUser(AbstractBaseUser):
    
    ROLE_CHOICES = [
        ('employee', 'Employee'),
        ('manager', 'Manager'),
    ]
    user_name         = models.CharField(max_length=50,unique=True)
    email             = models.EmailField(max_length=254,unique=True)
    role              = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Employee')
    password          = models.CharField(max_length=50)
    is_admin          = models.BooleanField(default=False)
    is_staff          = models.BooleanField(default=False)
    is_superuser      = models.BooleanField(default=False)
    is_active         = models.BooleanField(default=True)
    
    USERNAME_FIELD    = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.user_name},id->{self.id}"

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,add_label):
        return True
