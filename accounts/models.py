from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(_('email field'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.lastname} {self.firstname}"

class ScientificDirector(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.surname} {self.name}"


class Section(models.Model):
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"({self.short_name}) {self.name}"


class Competitor(models.Model):
    user_record = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    sc_director = models.ForeignKey(ScientificDirector,
                                    on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    section_number = models.IntegerField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.user_record.first_name} {self.user_record.last_name}"
