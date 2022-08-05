from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from common.models import Country, Region, Unit, District
from common.serializer import CountrySerializer, RegionSerializer, DistrictSerializer, UnitSerializer, UserSerializer, \
    CustomTokenObtainPairSerializer


class CountryList(APIView):
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class RegionList(APIView):
    def get(self, request, format=None):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)


class DistrictList(APIView):
    def get(self, request, format=None):
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)


class UnitList(APIView):
    def get(self, request, format=None):
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer