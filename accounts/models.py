from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('user must have an email address')
        if not username:
            raise ValueError('user must have an username')

        # create user object
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.is_active = True   # make user active by default
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )

        # now give the perms to the user
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True   # comes from PermissionsMixin
        user.is_active = True
        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, blank=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)  
    last_login = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # now this will be used for login the user not default username
    USERNAME_FIELD = 'email'

    # used while creating superuser
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # this model know to use myaccountmanager
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # when the user is admin then it will give all the permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    

# user profile
class UserProfile(models.Model):
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'