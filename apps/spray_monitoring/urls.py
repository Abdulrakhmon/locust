from django.urls import path

from spray_monitoring.views import SprayMonitoringActList, SprayMonitoringActAlbumCreation, \
    SprayMonitoringActAlbumDeletion, SprayMonitoringActDetail, SprayMonitoringActSpentInsecticideDeletion, \
    InsecticidesRemainderList, SprayMonitoringEfficiencyCreation, SprayMonitoringEfficiencyDeletion, \
    SprayMonitoringEfficiencyActCreation

urlpatterns = [
    path('act/list/', SprayMonitoringActList.as_view()),
    path('act/<int:pk>/detail/', SprayMonitoringActDetail.as_view()),
    path('act/<int:spray_monitoring_act_pk>/album-creation/', SprayMonitoringActAlbumCreation.as_view()),
    path('act/album/<int:pk>/delete/', SprayMonitoringActAlbumDeletion.as_view()),
    path('act/spent-insecticide/<int:pk>/delete/', SprayMonitoringActSpentInsecticideDeletion.as_view()),
    path('act/efficiency/<int:spray_monitoring_act_pk>/creation/', SprayMonitoringEfficiencyCreation.as_view()),
    path('act/efficiency/<int:pk>/deletion/', SprayMonitoringEfficiencyDeletion.as_view()),
    path('act/efficiency-act/<int:spray_monitoring_act_pk>/creation/', SprayMonitoringEfficiencyActCreation.as_view()),
    path('insecticides-remainder/list/', InsecticidesRemainderList.as_view()),
]
