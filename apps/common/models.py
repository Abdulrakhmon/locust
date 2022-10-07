# from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser

from apps.common.choices import UserStatus


class Country(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    alpha_two_code = models.CharField(max_length=2, unique=True)
    alpha_three_code = models.CharField(max_length=3, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        ordering = ('name_uz',)


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    geometry = models.MultiPolygonField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        ordering = ('name_uz',)


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    geometry = models.MultiPolygonField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        ordering = ('name_uz',)


class User(AbstractUser):
    email = models.CharField(null=True, blank=True, max_length=128)
    username = models.CharField(max_length=9, unique=True)
    name_uz = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    pin = models.CharField(max_length=14, unique=True)
    passport_series_and_number = models.CharField(max_length=9, unique=True)
    phone = models.CharField(max_length=9, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    districts = models.ManyToManyField(District, related_name='users', blank=True)
    status = models.IntegerField(choices=UserStatus.choices, default=UserStatus.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        ordering = ('name_uz',)


class Unit(models.Model):
    name_uz = models.CharField(max_length=8, unique=True)
    name_en = models.CharField(max_length=8, unique=True)
    name_ru = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        ordering = ('name_uz',)






