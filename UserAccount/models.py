from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from UserAccount.utils import ROLES, GENDER_CHOICES
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.modelfields import PhoneNumberField



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, first_name, last_name, mobile
        and password.
        """
        if not email:
            raise ValueError('User must have a email')

        if not password:
            raise ValueError('User must have a password')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        # user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a User with the given email, mobile
        and password
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_staff = True
        # user.is_admin = True
        user.is_superuser = True
        # user.is_active=True
        user.save(using=self._db)
        return user



class TimeStampMixin(models.Model):
    """Class representing the created_at and updated_at fields declared
    globally"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """This model will not create any Database Table"""
        abstract = True


# Create Custom User models.
class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):


    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)

    gender = models.CharField(
        max_length=11, choices=GENDER_CHOICES, null=False, blank=False)

    # Email field that serves as the username field
    email = models.EmailField(
        max_length=100, unique=True, blank=True, null=True)
    alternate_email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = PhoneNumberField(unique=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)
    is_new_user = models.BooleanField(default=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    role = models.CharField(max_length=50, choices=ROLES, default='user')
    profile_pic = models.FileField(
        upload_to="profile_pic", null=True, blank=True)
    is_superuser = models.BooleanField(
        ('superuser status'),
        default=False,
        help_text=(
            'Designates whether the user can log into this admin'
            ' site.',
        ),
    )
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=(
            'Designates whether the user can log into this admin'
            ' site.',
        ),
    )

    is_verified = models.BooleanField(
        null=False, blank=False, default=False)  # False = not verified
    google_id = models.CharField(max_length=255, null=True, blank=True)
    facebook_id = models.CharField(max_length=255, null=True, blank=True)
    

    # Setting email instead of username
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = USERNAME_FIELD

    # the default UserManager to make it work with our custom User Model
    objects = UserManager()

    def get_full_name(self):
        # Returns the first_name plus the last_name, with a space in between.
        full_name = None
        if self.first_name or self.last_name:
            full_name = self.first_name + " " + self.last_name

        else:
            full_name = self.email
        return full_name



    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'User'

