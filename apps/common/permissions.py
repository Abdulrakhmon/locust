from rest_framework import permissions

from survey.choices import SurveyStatus


class EditOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        groups = []
        if request.user and request.user.is_authenticated:
            if view.get_view_name() in ['Survey Detail', 'Spray Monitoring Act Detail']:
                groups = ['Republic Manager', 'Region Manager', 'Agronomist', 'Fumigator']

            if request.user.groups.filter(name__in=groups).exists():
                return True
            else:
                return False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and obj.status == SurveyStatus.APPROVED:
            return True
        elif obj.__class__.__name__ == 'Survey' and obj.agronomist == request.user and obj.status == SurveyStatus.SAVED:
            return True
        elif obj.__class__.__name__ == 'SprayMonitoringAct' and obj.fumigator == request.user and obj.status == SurveyStatus.SAVED:
            return True
        else:
            return False


class CreateOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        groups_read_only = []
        groups_can_create = []
        if request.user and request.user.is_authenticated:
            if view.get_view_name() in ['Survey List', 'Survey Detail', 'Survey Act Creation', 'Survey Album Creation']:
                groups_read_only = ['Republic Manager', 'Region Manager', 'Agronomist', 'Fumigator']
                groups_can_create = ['Agronomist']
            elif view.get_view_name() in ['Spray Monitoring Act List', 'Spray Monitoring Act Album Creation']:
                groups_read_only = ['Republic Manager', 'Region Manager', 'Agronomist', 'Fumigator']
                groups_can_create = ['Fumigator']

            if request.method in permissions.SAFE_METHODS and request.user.groups.filter(name__in=groups_read_only).exists():
                return True
            elif request.user.groups.filter(name__in=groups_can_create).exists():
                return True
            else:
                return False
        else:
            return False
