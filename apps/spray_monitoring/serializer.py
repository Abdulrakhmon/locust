from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer

from common.models import District
from common.serializer import UserPartialSerializer, DistrictSerializer
from spray_monitoring.models import ActiveSubstance, Formulation, Insecticide, Sprayer, ProtectiveClothing, \
    EmptyContainersStatus, SprayMonitoringAct, VegetationType, DamageLevel, SprayMonitoringActAlbum, SpentInsecticide
from survey.models import VegetationCover, LocustAge, Locust, LocustStage
from survey.serializer import VegetationCoverSerializer, LocustAgeSerializer, LocustSerializer, LocustStageSerializer


class ActiveSubstanceSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = ActiveSubstance


class FormulationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = Formulation


class InsecticideSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = Insecticide
        depth = 1


class InsecticidePartialSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = Insecticide
        depth = 1


class SprayerSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = Sprayer


class ProtectiveClothingSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = ProtectiveClothing


class EmptyContainersStatusSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = EmptyContainersStatus


class VegetationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = VegetationType


class DamageLevelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = DamageLevel


class SpentInsecticideSerializer(serializers.ModelSerializer):
    spray_monitoring_act = serializers.PrimaryKeyRelatedField(queryset=SprayMonitoringAct.objects.all(), many=False, write_only=True)

    insecticide_detail = InsecticideSerializer(read_only=True, source='insecticide', many=False)
    insecticide = serializers.PrimaryKeyRelatedField(queryset=Insecticide.objects.all(), many=False, write_only=True)

    class Meta:
        exclude = ['created_at', 'updated_at']
        model = SpentInsecticide


class SprayMonitoringActAlbumSerializer(serializers.ModelSerializer):
    spray_monitoring_act = serializers.PrimaryKeyRelatedField(queryset=SprayMonitoringAct.objects.all(), many=False, write_only=True)

    class Meta:
        exclude = ['created_at', 'updated_at']
        model = SprayMonitoringActAlbum


class SprayMonitoringActSerializer(serializers.ModelSerializer):
    district_detail = DistrictSerializer(read_only=True, source='district')
    district = serializers.PrimaryKeyRelatedField(queryset=District.objects.all(), many=False, write_only=True)
    fumigator = UserPartialSerializer(read_only=True)
    vegetation_type_detail = VegetationTypeSerializer(read_only=True, source='vegetation_type')
    vegetation_type = serializers.PrimaryKeyRelatedField(queryset=VegetationType.objects.all(), many=False, write_only=True)
    vegetation_cover_detail = VegetationCoverSerializer(read_only=True, source='vegetation_cover')
    vegetation_cover = serializers.PrimaryKeyRelatedField(queryset=VegetationCover.objects.all(), many=False, write_only=True)
    damage_level_detail = DamageLevelSerializer(read_only=True, source='damage_level')
    damage_level = serializers.PrimaryKeyRelatedField(queryset=DamageLevel.objects.all(), many=False, write_only=True)
    locust_age_detail = LocustAgeSerializer(read_only=True, source='locust_age')
    locust_detail = LocustSerializer(many=True, read_only=True, source='locust')
    locust = serializers.PrimaryKeyRelatedField(queryset=Locust.objects.all(), many=True, write_only=True)
    locust_age = serializers.PrimaryKeyRelatedField(queryset=LocustAge.objects.all(), many=False, write_only=True)
    locust_stage_detail = LocustStageSerializer(read_only=True, source='locust_stage', many=False)
    locust_stage = serializers.PrimaryKeyRelatedField(queryset=LocustStage.objects.all(), many=False, write_only=True)
    sprayer_detail = SprayerSerializer(read_only=True, source='sprayer', many=True)
    sprayer = serializers.PrimaryKeyRelatedField(queryset=Sprayer.objects.all(), many=True, write_only=True)
    protective_clothing_detail = ProtectiveClothingSerializer(many=True, read_only=True, source='protective_clothing')
    protective_clothing = serializers.PrimaryKeyRelatedField(queryset=ProtectiveClothing.objects.all(), many=True, write_only=True)
    empty_containers_status_detail = EmptyContainersStatusSerializer(many=True, read_only=True, source='empty_containers_status')
    empty_containers_status = serializers.PrimaryKeyRelatedField(queryset=EmptyContainersStatus.objects.all(), many=True, write_only=True)
    album = SprayMonitoringActAlbumSerializer(many=True, read_only=True)
    spent_insecticides = SpentInsecticideSerializer(many=True, read_only=True)

    class Meta:
        model = SprayMonitoringAct
        fields = '__all__'
