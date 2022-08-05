from django.db import models


class UserStatus(models.IntegerChoices):
    ACTIVE = 1, 'АКТИВНЫЙ'
    FIRED = 2, 'Уволенный'
    VACATION = 3, 'ОТПУСК'
    SICK = 4, 'БОЛЬНОЙ'
    INACTIVE = 5, 'Неактивный'
    PENDING = 6, 'В ПРОЦЕССЕ'