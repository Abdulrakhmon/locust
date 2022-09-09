from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from common.models import Country, District, Unit, Region


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = ['created_at', 'updated_at']


class RegionSerializer(GeoModelSerializer):
    class Meta:
        model = Region
        exclude = ['created_at', 'updated_at']


class RegionPartialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        exclude = ['country', 'geometry', 'created_at', 'updated_at']


class DistrictSerializer(GeoModelSerializer):
    class Meta:
        model = District
        exclude = ['created_at', 'updated_at']


class UserGroupSerializer(GeoModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserPartialSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['name_uz', 'name_en', 'name_ru', 'phone', 'pin', 'passport_series_and_number']


class UserSerializer(serializers.ModelSerializer):
    groups = UserGroupSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'name_uz', 'name_en', 'name_ru', 'phone', 'pin', 'passport_series_and_number', 'region', 'districts', 'groups']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        exclude = ['created_at', 'updated_at']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_detail'] = UserSerializer(self.user).data
        return data