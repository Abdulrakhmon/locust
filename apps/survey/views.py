from datetime import datetime, time

from django.db import connection
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from survey.choices import SurveyStatus
from survey.models import Biotope, Vegetation, VegetationCover, Locust, LocustStage, LocustAge, LocustAppearance, \
    NaturalEnemy, EggHatching, Behaviour, Fledging, Survey, SwarmDensity, SurveyAct, SurveyAlbum
from common.permissions import EditOrReadOnly, CreateOrReadOnly
from survey.serializer import BiotopeSerializer, VegetationSerializer, VegetationCoverSerializer, LocustSerializer, \
    LocustStageSerializer, LocustAgeSerializer, LocustAppearanceSerializer, NaturalEnemySerializer, \
    EggHatchingSerializer, BehaviourSerializer, FledgingSerializer, SurveySerializer, \
    LocustAppearanceDetailInfoSerializer, SurveyAlbumSerializer, SwarmDensitySerializer, SurveyActSerializer


class BiotopeList(APIView):
    def get(self, request, format=None):
        biotopes = Biotope.objects.all()
        serializer = BiotopeSerializer(biotopes, many=True)
        return Response(serializer.data)


class VegetationList(APIView):
    def get(self, request, format=None):
        vegetations = Vegetation.objects.all()
        serializer = VegetationSerializer(vegetations, many=True)
        return Response(serializer.data)


class VegetationCoverList(APIView):
    def get(self, request, format=None):
        vegetation_covers = VegetationCover.objects.all()
        serializer = VegetationCoverSerializer(vegetation_covers, many=True)
        return Response(serializer.data)


class LocustList(APIView):
    def get(self, request, format=None):
        locusts = Locust.objects.all()
        serializer = LocustSerializer(locusts, many=True)
        return Response(serializer.data)


class LocustStageList(APIView):
    def get(self, request, format=None):
        locust_stages = LocustStage.objects.all()
        serializer = LocustStageSerializer(locust_stages, many=True)
        return Response(serializer.data)


class LocustAgeList(APIView):
    def get(self, request, format=None):
        locust_ages = LocustAge.objects.all()
        serializer = LocustAgeSerializer(locust_ages, many=True)
        return Response(serializer.data)


class LocustAppearanceList(APIView):
    def get(self, request, format=None):
        locust_appearances = LocustAppearance.objects.all()
        serializer = LocustAppearanceSerializer(locust_appearances, many=True)
        return Response(serializer.data)


class NaturalEnemyList(APIView):
    def get(self, request, format=None):
        natural_enemies = NaturalEnemy.objects.all()
        serializer = NaturalEnemySerializer(natural_enemies, many=True)
        return Response(serializer.data)


class EggHatchingList(APIView):
    def get(self, request, format=None):
        egg_hatchings = EggHatching.objects.all()
        serializer = EggHatchingSerializer(egg_hatchings, many=True)
        return Response(serializer.data)


class BehaviourList(APIView):
    def get(self, request, format=None):
        behaviours = Behaviour.objects.all()
        serializer = BehaviourSerializer(behaviours, many=True)
        return Response(serializer.data)


class FledgingList(APIView):
    def get(self, request, format=None):
        fledgings = Fledging.objects.all()
        serializer = FledgingSerializer(fledgings, many=True)
        return Response(serializer.data)


class SwarmDensityList(APIView):
    def get(self, request, format=None):
        swarm_densities = SwarmDensity.objects.all()
        serializer = SwarmDensitySerializer(swarm_densities, many=True)
        return Response(serializer.data)


class SurveyList(APIView, LimitOffsetPagination):

    """
    get:
    Query params for filter: survey_act_number,  survey_act_is_null(False -> retrieve surveys do not have acts; True -> retrieve surveys which have acts),
    locust(id, ManyToMany: ?locust=1&locust=3), region(id),
    locust_appearance(id, ManyToMany: ?locust_appearance=1&locust_appearance=3),
    approved_at_gte<=>approved_at_lte(YYYY-MM-DD), act_given_date_gte<=>act_given_date_lte(YYYY-MM-DD),
    """
    permission_classes = [CreateOrReadOnly]

    def get(self, request, format=None):
        query_strings = request.GET
        user = request.user

        surveys = Survey.objects.filter(Q(status=SurveyStatus.APPROVED) | Q(agronomist=user))
        # surveys = Survey.objects.select_related('locust_appearance_detail_info', 'act').prefetch_related('album')

        if query_strings.get('survey_act_number'):
            surveys = surveys.filter(act__number=query_strings.get('survey_act_number'))
        else:
            if query_strings.get('survey_act_is_null'):
                if query_strings.get('survey_act_is_null') == 'False':
                    surveys = surveys.filter(act__isnull=False)
                elif query_strings.get('survey_act_is_null') == 'True':
                    surveys = surveys.filter(act__isnull=True)

            if query_strings.getlist('locust[]'):
                surveys = surveys.filter(locust__in=query_strings.getlist('locust[]'))

            if query_strings.getlist('locust_appearance[]'):
                surveys = surveys.filter(locust_appearance__in=query_strings.getlist('locust_appearance'))

            if query_strings.get('approved_at_gte') and query_strings.get('approved_at_lte'):
                surveys = surveys.filter(approved_at__gte=query_strings.get('approved_at_gte'),
                                         approved_at__lte=str(query_strings.get('approved_at_lte') + ' 23:59:59'))

            if query_strings.get('act_given_date_gte') and query_strings.get('act_given_date_lte'):
                surveys = surveys.filter(act__isnull=False,
                                         act__given_date__gte=query_strings.get('act_given_date_gte'),
                                         act__given_date__lte=str(query_strings.get('act_given_date_lte')))

            if user.region:
                surveys = surveys.filter(district__region=user.region)
            elif query_strings.get('region'):
                surveys = surveys.filter(district__region__id=query_strings.get('region'))

        surveys = self.paginate_queryset(surveys.distinct('pk'), request, view=self)
        serializer = SurveySerializer(surveys, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            try:
                detail_info_serializer = LocustAppearanceDetailInfoSerializer(data=request.data['locust_appearance_detail_info'])
                if detail_info_serializer.is_valid():
                    instance = serializer.save(agronomist=self.request.user)
                    detail_info_serializer.save(survey=instance)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(detail_info_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyAlbumCreation(APIView):
    """
    Create a survey album instance.
    """
    permission_classes = [CreateOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, survey_pk, format=None):
        get_object_or_404(Survey, pk=survey_pk, agronomist=request.user, status=SurveyStatus.SAVED)
        errors = []
        if request.FILES.getlist('album'):
            for image in request.FILES.getlist('album'):
                serializer = SurveyAlbumSerializer(data={'image': image, 'survey': survey_pk})
                if serializer.is_valid():
                    serializer.save()
                else:
                    errors.append(serializer.errors)
        else:
            return Response({"album": ["This field may not be null."]}, status=status.HTTP_404_NOT_FOUND)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_201_CREATED)


class SurveyAlbumDeletion(APIView):
    """
    Delete a survey album instance.
    """
    def delete(self, request, pk, format=None):
        album_image = get_object_or_404(SurveyAlbum, pk=pk, survey__agronomist=request.user, survey__status=SurveyStatus.SAVED)
        if album_image.image:
            album_image.image.delete()
        album_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SurveyDetail(APIView):
    """
    Retrieve, update or delete a survey instance.
    """
    permission_classes = [EditOrReadOnly]

    def get_object(self, pk, request):
        instance = get_object_or_404(Survey, pk=pk)
        self.check_object_permissions(request=request, obj=instance)  # beacuse of APIView, has_object_permission is checked manually
        return instance

    def get(self, request, pk, format=None):
        instance = self.get_object(pk=pk, request=request)
        serializer = SurveySerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk=pk, request=request)
        serializer = SurveySerializer(instance, data=request.data)
        if serializer.is_valid():
            try:
                detail_info_serializer = LocustAppearanceDetailInfoSerializer(instance.locust_appearance_detail_info, data=request.data['locust_appearance_detail_info'])
                if detail_info_serializer.is_valid():
                    serializer.save()
                    detail_info_serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(detail_info_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk, request=request)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, format=None):
        instance = self.get_object(pk=pk, request=request)
        instance.status = SurveyStatus.APPROVED
        instance.approved_at = datetime.now()
        instance.save()
        return Response(status=status.HTTP_202_ACCEPTED)


class SurveyActCreation(APIView):
    permission_classes = [CreateOrReadOnly]

    def post(self, request, survey_pk, format=None):
        user = request.user
        region = user.region

        survey = get_object_or_404(Survey, pk=survey_pk, agronomist=user, status=SurveyStatus.APPROVED, act__isnull=True)

        try:
            this_year = int(datetime.now().strftime('%y'))
            if int(region.pk) < 10:
                first_four_digits = str(this_year) + '0' + str(region.pk)
            else:
                first_four_digits = str(this_year) + str(region.pk)
            last_survey_act = SurveyAct.objects.filter(number__startswith=first_four_digits).order_by('number').last()

            if last_survey_act:
                number = str(int(last_survey_act.number) + 1)
            else:
                number = this_year * 1000000000 + int(region.pk) * 10000000 + 1

            instance = SurveyAct.objects.create(
                survey=survey,
                number=number,
                agronomist=user,
            )

            serializer = SurveyActSerializer(instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
