from django.urls import path
from survey.views import SurveyList, SurveyDetail, SurveyAlbumCreation, SurveyAlbumDeletion, SurveyActCreation

urlpatterns = [
    path('list/', SurveyList.as_view()),
    path('<int:pk>/detail/', SurveyDetail.as_view()),
    path('<int:survey_pk>/album-creation/', SurveyAlbumCreation.as_view()),
    path('album/<int:pk>/delete/', SurveyAlbumDeletion.as_view()),
    path('act/<int:survey_pk>/create/', SurveyActCreation.as_view()),
]
