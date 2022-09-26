from django.db import transaction
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_gis.serializers import GeoModelSerializer

from common.models import District
from common.serializer import UserSerializer, DistrictSerializer, UserPartialSerializer
from survey.models import Biotope, Vegetation, VegetationCover, Locust, LocustStage, LocustAge, LocustAppearance, \
    NaturalEnemy, EggHatching, Behaviour, Fledging, Survey, LocustAppearanceDetailInfo, SurveyAct, SurveyAlbum, \
    SwarmDensity


class BiotopeSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = Biotope


class VegetationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = Vegetation


class VegetationCoverSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = VegetationCover


class LocustSerializer(serializers.ModelSerializer):
    album = serializers.StringRelatedField(many=True)

    class Meta:
        exclude = ['created_at', 'updated_at']
        model = Locust


class LocustStageSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = LocustStage


class LocustAgeSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = LocustAge


class LocustAppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = LocustAppearance


class NaturalEnemySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = NaturalEnemy


class EggHatchingSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = EggHatching


class BehaviourSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = Behaviour


class FledgingSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = Fledging


class SwarmDensitySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']
        model = SwarmDensity


class SurveyAlbumSerializer(serializers.ModelSerializer):
    survey = serializers.PrimaryKeyRelatedField(queryset=Survey.objects.all(), many=False, write_only=True)

    class Meta:
        exclude = ['created_at', 'updated_at']
        model = SurveyAlbum


class LocustAppearanceDetailInfoSerializer(serializers.ModelSerializer):
    egg_hatching_detail = EggHatchingSerializer(read_only=True, source='egg_hatching')
    egg_hatching = serializers.PrimaryKeyRelatedField(queryset=EggHatching.objects.all(), many=False, write_only=True, allow_null=True)
    hopper_age_detail = LocustAgeSerializer(read_only=True, source='hopper_age')
    hopper_age = serializers.PrimaryKeyRelatedField(queryset=LocustAge.objects.all(), many=False, write_only=True, allow_null=True)
    hopper_stage_detail = LocustStageSerializer(read_only=True, source='hopper_stage')
    hopper_stage = serializers.PrimaryKeyRelatedField(queryset=LocustStage.objects.all(), many=False, write_only=True, allow_null=True)
    behaviour_detail = BehaviourSerializer(read_only=True, source='behaviour')
    behaviour = serializers.PrimaryKeyRelatedField(queryset=Behaviour.objects.all(), many=False, write_only=True, allow_null=True)
    hopper_age_in_band_detail = LocustAgeSerializer(read_only=True, source='hopper_age_in_band')
    hopper_age_in_band = serializers.PrimaryKeyRelatedField(queryset=LocustAge.objects.all(), many=False, write_only=True, allow_null=True)
    adult_fledging_detail = FledgingSerializer(read_only=True, source='adult_fledging')
    adult_fledging = serializers.PrimaryKeyRelatedField(queryset=Fledging.objects.all(), many=False, write_only=True, allow_null=True)
    adult_stage_detail = LocustStageSerializer(read_only=True, source='adult_stage')
    adult_stage = serializers.PrimaryKeyRelatedField(queryset=LocustStage.objects.all(), many=False, write_only=True, allow_null=True)
    natural_enemies_detail = NaturalEnemySerializer(many=True, read_only=True, source='natural_enemies')
    natural_enemies = serializers.PrimaryKeyRelatedField(queryset=NaturalEnemy.objects.all(), many=True, write_only=True, allow_null=True)
    swarm_density_detail = SwarmDensitySerializer(read_only=True, source='swarm_density')
    swarm_density = serializers.PrimaryKeyRelatedField(queryset=SwarmDensity.objects.all(), many=False, write_only=True, allow_null=True)

    class Meta:
        exclude = ['survey']
        model = LocustAppearanceDetailInfo


class SurveyActSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['number', 'given_date']
        model = SurveyAct


class SurveySerializer(serializers.ModelSerializer):
    agronomist = UserPartialSerializer(read_only=True)
    biotope_detail = BiotopeSerializer(read_only=True, source='biotope')
    biotope = serializers.PrimaryKeyRelatedField(queryset=Biotope.objects.all(), many=False, write_only=True)
    vegetation_detail = VegetationSerializer(read_only=True, source='vegetation')
    vegetation = serializers.PrimaryKeyRelatedField(queryset=Vegetation.objects.all(), many=False, write_only=True)
    vegetation_cover_detail = VegetationCoverSerializer(read_only=True, source='vegetation_cover')
    vegetation_cover = serializers.PrimaryKeyRelatedField(queryset=VegetationCover.objects.all(), many=False, write_only=True)
    district_detail = DistrictSerializer(read_only=True, source='district')
    district = serializers.PrimaryKeyRelatedField(queryset=District.objects.all(), many=False, write_only=True)
    album = SurveyAlbumSerializer(many=True, read_only=True)
    locust_appearance_detail_info = LocustAppearanceDetailInfoSerializer(read_only=True)
    act = SurveyActSerializer(read_only=True)
    locust_detail = LocustSerializer(many=True, read_only=True, source='locust')
    locust = serializers.PrimaryKeyRelatedField(queryset=Locust.objects.all(), many=True, write_only=True)
    locust_appearance_detail = LocustAppearanceSerializer(many=True, read_only=True, source='locust_appearance')
    locust_appearance = serializers.PrimaryKeyRelatedField(queryset=LocustAppearance.objects.all(), many=True, write_only=True)

    class Meta:
        model = Survey
        fields = '__all__'

    # def create(self, validated_data):
    #     try:
    #         with transaction.atomic():
    #             serializer = LocustAppearanceDetailInfoSerializer(data=self.context['locust_appearance_detail_info'])
    #             if serializer.is_valid():
    #                 instance = super().create(validated_data)
    #                 serializer.save(survey=instance)
    #                 return instance
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         return Response(e, status=status.HTTP_400_BAD_REQUEST)