from datetime import datetime

from django.db.models import Q, Sum
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models import Region
from common.permissions import CreateOrReadOnly, EditOrReadOnly
from common.serializer import RegionPartialSerializer
from spray_monitoring.choices import SprayMonitoringStatus
from spray_monitoring.models import ActiveSubstance, Formulation, Insecticide, Sprayer, ProtectiveClothing, \
    EmptyContainersStatus, SprayMonitoringAct, SprayMonitoringActAlbum, SpentInsecticide, InsecticidesYearlyRemainder, \
    InsecticideExchange, VegetationType, DamageLevel, SprayMonitoringEfficiency, SprayMonitoringEfficiencyAct
from spray_monitoring.serializer import ActiveSubstanceSerializer, FormulationSerializer, InsecticideSerializer, \
    SprayerSerializer, ProtectiveClothingSerializer, EmptyContainersStatusSerializer, SprayMonitoringActSerializer, \
    SpentInsecticideSerializer, SprayMonitoringActAlbumSerializer, DamageLevelSerializer, VegetationTypeSerializer, \
    SprayMonitoringEfficiencySerializer, SprayMonitoringEfficiencyActSerializer


class ActiveSubstanceList(APIView):
    def get(self, request, format=None):
        active_substances = ActiveSubstance.objects.all()
        serializer = ActiveSubstanceSerializer(active_substances, many=True)
        return Response(serializer.data)


class FormulationList(APIView):
    def get(self, request, format=None):
        formulations = Formulation.objects.all()
        serializer = FormulationSerializer(formulations, many=True)
        return Response(serializer.data)


class InsecticideList(APIView):
    def get(self, request, format=None):
        insecticides = Insecticide.objects.all()
        serializer = InsecticideSerializer(insecticides, many=True)
        return Response(serializer.data)


class VegetationTypeList(APIView):
    def get(self, request, format=None):
        vegetation_types = VegetationType.objects.all()
        serializer = VegetationTypeSerializer(vegetation_types, many=True)
        return Response(serializer.data)


class DamageLevelList(APIView):
    def get(self, request, format=None):
        damage_levels = DamageLevel.objects.all()
        serializer = DamageLevelSerializer(damage_levels, many=True)
        return Response(serializer.data)


class SprayerList(APIView):
    def get(self, request, format=None):
        sprayers = Sprayer.objects.all()
        serializer = SprayerSerializer(sprayers, many=True)
        return Response(serializer.data)


class ProtectiveClothingList(APIView):
    def get(self, request, format=None):
        protective_clothing = ProtectiveClothing.objects.all()
        serializer = ProtectiveClothingSerializer(protective_clothing, many=True)
        return Response(serializer.data)


class EmptyContainersStatusList(APIView):
    def get(self, request, format=None):
        empty_containers_statuses = EmptyContainersStatus.objects.all()
        serializer = EmptyContainersStatusSerializer(empty_containers_statuses, many=True)
        return Response(serializer.data)


class InsecticidesRemainderList(APIView):
    def get(self, request, format=None):
        year = f"{datetime.today().year}-01-01"

        insecticides_remainder_list_grouped_by_region = {}

        for region in Region.objects.all():
            insecticides_remainder_list_grouped_by_region[region.pk] = []

        insecticide_remainder_dict = {"insecticide_info": None, "spent_insecticide_amount": None,
                                      "sent_insecticide_amount": None, "received_insecticide_amount": None,
                                      "insecticide_remainder": None}

        insecticides_yearly_remainders = InsecticidesYearlyRemainder.objects.filter(year=year)

        if request.user.region:
            insecticides_yearly_remainders = insecticides_yearly_remainders.filter(region=request.user.region)
        else:
            insecticides_yearly_remainders = insecticides_yearly_remainders.order_by('region')
        for insecticides_yearly_remainder in insecticides_yearly_remainders:
            insecticide_remainder_dict['spent_insecticide_amount'] = SpentInsecticide.objects.filter(insecticide=insecticides_yearly_remainder.insecticide,
                                                                        spray_monitoring_act__status=SprayMonitoringStatus.APPROVED,
                                                                        spray_monitoring_act__district__region=insecticides_yearly_remainder.region,
                                                                        spray_monitoring_act__given_date__gte=insecticides_yearly_remainder.year).aggregate(Sum('amount'))['amount__sum'] or 0
            insecticide_remainder_dict['sent_insecticide_amount'] = InsecticideExchange.objects.filter(insecticide=insecticides_yearly_remainder.insecticide,
                                                                          is_approved=True,
                                                                          sender_region=insecticides_yearly_remainder.region,
                                                                          given_date__gte=insecticides_yearly_remainder.year).aggregate(Sum('amount'))['amount__sum'] or 0
            insecticide_remainder_dict['received_insecticide_amount'] = InsecticideExchange.objects.filter(insecticide=insecticides_yearly_remainder.insecticide,
                                                                              is_approved=True,
                                                                              receiver_region=insecticides_yearly_remainder.region,
                                                                              given_date__gte=insecticides_yearly_remainder.year).aggregate(Sum('amount'))['amount__sum'] or 0
            insecticide_remainder_dict['insecticide_info'] = InsecticideSerializer(insecticides_yearly_remainder.insecticide).data
            insecticide_remainder_dict['insecticide_remainder'] = insecticides_yearly_remainder.amount + insecticide_remainder_dict['received_insecticide_amount'] - insecticide_remainder_dict['spent_insecticide_amount'] - insecticide_remainder_dict['sent_insecticide_amount']

            insecticides_remainder_list_grouped_by_region[insecticides_yearly_remainder.region.pk].append(insecticide_remainder_dict)
            insecticide_remainder_dict = {"insecticide_info": None, "spent_insecticide_amount": None,
                                          "sent_insecticide_amount": None, "received_insecticide_amount": None,
                                          "insecticide_remainder": None}

        return Response(insecticides_remainder_list_grouped_by_region)


class SprayMonitoringActList(APIView, LimitOffsetPagination):

    """
    get:
    Query params for filter: number, damage_level(id), locust(id, ManyToMany: ?locust=1&locust=3),
    region(id), given_date_gte<=>given_date_lte(YYYY-MM-DD)
    """
    permission_classes = [CreateOrReadOnly]

    def get(self, request, format=None):
        query_strings = request.GET
        user = request.user

        # start_queries = len(connection.queries)

        spray_monitoring_acts = SprayMonitoringAct.objects.filter(Q(status=SprayMonitoringStatus.APPROVED) | Q(fumigator=user))
        # spray_monitoring_acts = SprayMonitoringAct.objects.prefetch_related('spent_insecticides', 'album')
        if query_strings.get('number'):
            spray_monitoring_acts = spray_monitoring_acts.filter(number=query_strings.get('number'))
        else:
            if query_strings.get('damage_level'):
                spray_monitoring_acts = spray_monitoring_acts.filter(damage_level=query_strings.get('damage_level'))

            if query_strings.getlist('locust[]'):
                spray_monitoring_acts = spray_monitoring_acts.filter(locust__in=query_strings.getlist('locust[]'))

            if query_strings.get('given_date_gte') and query_strings.get('given_date_gte'):
                spray_monitoring_acts = spray_monitoring_acts.filter(given_date__gte=query_strings.get('given_date_gte'),
                                                                     given_date__lte=str(query_strings.get('given_date_lte')))

            if user.region:
                spray_monitoring_acts = spray_monitoring_acts.filter(district__region=user.region)
            elif query_strings.get('region'):
                spray_monitoring_acts = spray_monitoring_acts.filter(district__region__id=query_strings.get('region'))

        spray_monitoring_acts = self.paginate_queryset(spray_monitoring_acts.order_by('pk').distinct('pk'), request, view=self)
        serializer = SprayMonitoringActSerializer(spray_monitoring_acts, many=True)

        # end_queries = len(connection.queries)
        # print(f"Number of Queries : {end_queries} - {start_queries} = {end_queries - start_queries}")

        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SprayMonitoringActSerializer(data=request.data)
        if serializer.is_valid():
            try:
                instance = serializer.save(fumigator=self.request.user)
                for spent_insecticide in request.data['spent_insecticides']:
                    spent_insecticide['spray_monitoring_act'] = instance.pk
                    spent_insecticide_serializer = SpentInsecticideSerializer(data=spent_insecticide)
                    if spent_insecticide_serializer.is_valid():
                        spent_insecticide_serializer.save()
                    else:
                        instance.delete()
                        return Response(spent_insecticide_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SprayMonitoringActDetail(APIView):
    """
    Retrieve, update or delete a survey instance.
    """
    permission_classes = [EditOrReadOnly]

    def get_object(self, pk, request):
        instance = get_object_or_404(SprayMonitoringAct, pk=pk, spent_insecticides__isnull=False)   # spent_insecticides is required
        self.check_object_permissions(request=request, obj=instance)  # beacuse of APIView, has_object_permission is checked manually
        return instance

    def get(self, request, pk, format=None):
        instance = self.get_object(pk=pk, request=request)
        serializer = SprayMonitoringActSerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk=pk, request=request)
        serializer = SprayMonitoringActSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                for spent_insecticide in request.data['spent_insecticides']:
                    spent_insecticide['spray_monitoring_act'] = pk
                    try:
                        spent_insecticide_instance = SpentInsecticide.objects.get(pk=spent_insecticide['id'])
                        spent_insecticide_serializer = SpentInsecticideSerializer(spent_insecticide_instance, data=spent_insecticide)
                        if spent_insecticide_serializer.is_valid():
                            spent_insecticide_serializer.save()
                        else:
                            return Response(spent_insecticide_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    except Exception as e:
                        spent_insecticide_serializer = SpentInsecticideSerializer(data=spent_insecticide)
                        if spent_insecticide_serializer.is_valid():
                            spent_insecticide_serializer.save()
                        else:
                            return Response(spent_insecticide_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk, request=request)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, format=None):
        instance = self.get_object(pk=pk, request=request)
        region = instance.district.region
        try:
            this_year = int(datetime.now().strftime('%y'))
            if int(region.pk) < 10:
                first_four_digits = str(this_year) + '0' + str(region.pk)
            else:
                first_four_digits = str(this_year) + str(region.pk)
            last_instance = SprayMonitoringAct.objects.filter(number__startswith=first_four_digits).order_by('number').last()

            if last_instance:
                number = str(int(last_instance.number) + 1)
            else:
                number = this_year * 1000000000 + int(region.pk) * 10000000 + 1

            instance.number = number
            instance.given_date = datetime.today()
            instance.status = SprayMonitoringStatus.APPROVED
            instance.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SprayMonitoringActSpentInsecticideDeletion(APIView):

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(SpentInsecticide, pk=pk, spray_monitoring_act__fumigator=request.user, spray_monitoring_act__status=SprayMonitoringStatus.SAVED)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SprayMonitoringActAlbumCreation(APIView):
    permission_classes = [CreateOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, spray_monitoring_act_pk, format=None):
        get_object_or_404(SprayMonitoringAct, pk=spray_monitoring_act_pk, fumigator=request.user, status=SprayMonitoringStatus.SAVED)
        errors = []
        if request.FILES.getlist('album'):
            for image in request.FILES.getlist('album'):
                serializer = SprayMonitoringActAlbumSerializer(data={'image': image, 'spray_monitoring_act': spray_monitoring_act_pk})
                if serializer.is_valid():
                    serializer.save()
                else:
                    errors.append(serializer.errors)

            if errors:
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({"album": ["This field may not be null."]}, status=status.HTTP_404_NOT_FOUND)


class SprayMonitoringActAlbumDeletion(APIView):

    def delete(self, request, pk, format=None):
        album_image = get_object_or_404(SprayMonitoringActAlbum, pk=pk, spray_monitoring_act__fumigator=request.user, spray_monitoring_act__status=SprayMonitoringStatus.SAVED)
        if album_image.image:
            album_image.image.delete()
        album_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SprayMonitoringEfficiencyCreation(APIView):
    permission_classes = [CreateOrReadOnly]

    def post(self, request, spray_monitoring_act_pk, format=None):
        spray_monitoring_act = get_object_or_404(SprayMonitoringAct, pk=spray_monitoring_act_pk, fumigator=request.user,
                                                 status=SprayMonitoringStatus.APPROVED, efficiency_act__isnull=True)
        try:
            serializer = SprayMonitoringEfficiencySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(spray_monitoring_act=spray_monitoring_act)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class SprayMonitoringEfficiencyDeletion(APIView):

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(SprayMonitoringEfficiency, pk=pk, spray_monitoring_act__fumigator=request.user,
                                     status=SprayMonitoringStatus.APPROVED, spray_monitoring_act__efficiency_act__isnull=True)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SprayMonitoringEfficiencyActCreation(APIView):
    """
    Retrieve, update or delete a survey instance.
    """
    permission_classes = [CreateOrReadOnly]

    def post(self, request, spray_monitoring_act_pk, format=None):
        user = request.user
        region = user.region

        spray_monitoring_act = get_object_or_404(SprayMonitoringAct, pk=spray_monitoring_act_pk, fumigator=user,
                                                 status=SprayMonitoringStatus.APPROVED, efficiencies__isnull=False,
                                                 efficiency_act__isnull=True)

        try:
            this_year = int(datetime.now().strftime('%y'))
            if int(region.pk) < 10:
                first_four_digits = str(this_year) + '0' + str(region.pk)
            else:
                first_four_digits = str(this_year) + str(region.pk)

            last_spray_monitoring_efficiency_act = SprayMonitoringEfficiencyAct.objects.filter(number__startswith=first_four_digits).order_by('number').last()

            if last_spray_monitoring_efficiency_act:
                number = str(int(last_spray_monitoring_efficiency_act.number) + 1)
            else:
                number = this_year * 1000000000 + int(region.pk) * 10000000 + 1
            instance = SprayMonitoringEfficiencyAct.objects.create(
                spray_monitoring_act=spray_monitoring_act,
                number=number,
            )

            serializer = SprayMonitoringEfficiencyActSerializer(instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
