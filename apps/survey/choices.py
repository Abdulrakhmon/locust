from django.db import models


class SurveyStatus(models.IntegerChoices):
    SAVED = 1, 'Сохранено'
    APPROVED = 2, 'Одобренный'