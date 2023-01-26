from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# create manager class
class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """

    # if not specify password, it will be set default as none
    def create_user(self, email, name, password = None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # to hash password, to make sure password is safe

        # To save changes to an object that's already in the database
        # This performs an UPDATE SQL statement behind the scenes
        user.save(using = self._db) # standard save objects in django

        return user

    def create_superuser(self, email, name, password):
        """ Create and save a new superuser with given details """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user





# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_activate = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    # speficy the model manager for the user model
    # to create user, manage user
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve full name of user """
        return self.name

    def get_short_name(self):
        """ Retrieve short name of user """
        # since we don't have a way to define a short name
        # currently return the same thing as above
        return self.name

    # Recommend for all django model
    # 1. The __str__ method just tells Django what to print when it needs to print out an instance of the any model
    # 2. In a model, without this funtion, in real database, this model will be store as UserProfileModel Object(1)
    # but with this function, model will be savd as a specific name (eg: something)
    def __str__(self):
        """ Return string representation of our user """
        return self.email
