from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
USER_TYPE_CHOICES = (
        (1, 'CUSTOMER'),
        (2, 'ADMIN'),
    )

class UserManager(BaseUserManager):

    def create_user(self, email, password=None,user_type=1,name='',is_staff=False, is_superuser=False):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.localtime(timezone.now())
        email=self.normalize_email(email)
        user = self.model(
            name=name,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            user_type=user_type,
        
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
   
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, True, True, **extra_fields)
        user.admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)
    city = models.CharField(max_length=254, null=True, blank=True)
    state = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=254, null=True, blank=True)
    referral_code = models.CharField(max_length=10, null=True, blank=True,unique=True)
    
    

    def __str__(self):
        return self.user.email

