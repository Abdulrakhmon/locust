"""locust URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view

from common.views import CountryList, RegionList, DistrictList, CustomTokenObtainPairView
from spray_monitoring.views import ActiveSubstanceList, FormulationList, InsecticideList, SprayerList, \
    ProtectiveClothingList, EmptyContainersStatusList, VegetationTypeList, DamageLevelList
from survey.views import FledgingList, BehaviourList, EggHatchingList, NaturalEnemyList, LocustAppearanceList, \
    LocustAgeList, LocustStageList, LocustList, VegetationCoverList, VegetationList, BiotopeList, SwarmDensityList

swagger_schema_view = get_swagger_view(title='Locust API')
schema_view = get_schema_view(title='Locust API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/documentation/', swagger_schema_view),
    path('v2/documentation/', include_docs_urls(title='Locust API')),
    path('schema/', schema_view),
    path('dictionary/countries/', CountryList.as_view()),
    path('dictionary/regions/', RegionList.as_view()),
    path('dictionary/districts/', DistrictList.as_view()),
    path('dictionary/active-substances/', ActiveSubstanceList.as_view()),
    path('dictionary/formulations/', FormulationList.as_view()),
    path('dictionary/insecticides/', InsecticideList.as_view()),
    path('dictionary/vegetation-types/', VegetationTypeList.as_view()),
    path('dictionary/damage-levels/', DamageLevelList.as_view()),
    path('dictionary/sprayers/', SprayerList.as_view()),
    path('dictionary/protective-clothing/', ProtectiveClothingList.as_view()),
    path('dictionary/empty-containers-statuses/', EmptyContainersStatusList.as_view()),
    path('dictionary/biotopes/', BiotopeList.as_view()),
    path('dictionary/vegetations/', VegetationList.as_view()),
    path('dictionary/vegetation-covers/', VegetationCoverList.as_view()),
    path('dictionary/locusts/', LocustList.as_view()),
    path('dictionary/locust-stages/', LocustStageList.as_view()),
    path('dictionary/locust-ages/', LocustAgeList.as_view()),
    path('dictionary/locust-appearances/', LocustAppearanceList.as_view()),
    path('dictionary/natural-enemies/', NaturalEnemyList.as_view()),
    path('dictionary/egg-hatchings/', EggHatchingList.as_view()),
    path('dictionary/behaviours/', BehaviourList.as_view()),
    path('dictionary/fledgings/', FledgingList.as_view()),
    path('dictionary/swarm-density/', SwarmDensityList.as_view()),
    # path('', include(('common.urls', 'common'), namespace='common')),
    path('survey/', include(('survey.urls', 'survey'), namespace='survey')),
    path('spray-monitoring/', include(('spray_monitoring.urls', 'spray_monitoring'), namespace='spray-monitoring')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
