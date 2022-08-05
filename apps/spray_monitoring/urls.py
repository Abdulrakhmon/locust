from django.urls import path

from spray_monitoring.views import SprayMonitoringActList, SprayMonitoringActAlbumCreation, \
    SprayMonitoringActAlbumDeletion, SprayMonitoringActDetail, SprayMonitoringActSpentInsecticideDeletion, \
    InsecticidesRemainderList

urlpatterns = [
    path('act/list/', SprayMonitoringActList.as_view()),
    path('act/<int:pk>/detail/', SprayMonitoringActDetail.as_view()),
    path('act/<int:spray_monitoring_act_pk>/album-creation/', SprayMonitoringActAlbumCreation.as_view()),
    path('act/album/<int:pk>/delete/', SprayMonitoringActAlbumDeletion.as_view()),
    path('act/spent-insecticide/<int:pk>/delete/', SprayMonitoringActSpentInsecticideDeletion.as_view()),
    path('insecticides-remainder/list/', InsecticidesRemainderList.as_view()),
    # path('act/<int:survey_pk>/create/', SurveyActCreation.as_view()),
]
