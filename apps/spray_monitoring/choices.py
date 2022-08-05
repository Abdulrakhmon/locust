from django.db import models


class SprayMonitoringStatus(models.IntegerChoices):
    SAVED = 1, 'Сохранено'
    APPROVED = 2, 'Одобренный'