# from django.db import models

from django.conf import settings
from django.contrib.gis.db import models

from common.managers import IsActiveManager
from common.models import District, Unit, Region
from spray_monitoring.choices import SprayMonitoringStatus
from survey.models import VegetationCover, Locust, LocustAge, LocustStage


class ActiveSubstance(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Действующее вещество'
        ordering = ['name_uz']
        db_table = 'active_substance'


class Formulation(models.Model):
    alpha_code_uz = models.CharField(max_length=8, unique=True)
    alpha_code_en = models.CharField(max_length=8, unique=True)
    alpha_code_ru = models.CharField(max_length=8, unique=True)
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Препаративная форма'
        ordering = ['name_uz']
        db_table = 'formulation'


class Insecticide(models.Model):
    active_substance = models.ForeignKey(ActiveSubstance, on_delete=models.CASCADE, related_name='insecticides')
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    concentration = models.CharField(max_length=3)
    formulation = models.ForeignKey(Formulation, on_delete=models.CASCADE, related_name='+')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='+')
    is_active = models.BooleanField(default=True)
    min_dose = models.DecimalField(max_digits=7, decimal_places=3)
    mid_dose = models.DecimalField(max_digits=7, decimal_places=3)
    max_dose = models.DecimalField(max_digits=7, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = IsActiveManager()

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Информация об инсектицидах(Коммерческое название)'
        ordering = ['name_uz']
        db_table = 'insecticide'


class InsecticideExchange(models.Model):
    insecticide = models.ForeignKey(Insecticide, on_delete=models.CASCADE, related_name='insecticide_exchanges')
    sender_region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    receiver_region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    given_date = models.DateField()
    note = models.CharField(max_length=512)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'insecticide_exchange'


class InsecticidesYearlyRemainder(models.Model):
    insecticide = models.ForeignKey(Insecticide, on_delete=models.CASCADE, related_name='+')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='insecticides_yearly_remainders')
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    year = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.insecticide.name_uz

    class Meta:
        constraints = [models.UniqueConstraint(fields=['insecticide', 'region', 'year'], name='unique_insecticide_yearly_remainder')]
        db_table = 'insecticides_yearly_remainder'


class VegetationType(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Растительность Тип'
        ordering = ['name_uz']
        db_table = 'vegetation_type'


class DamageLevel(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Поврежденность'
        ordering = ['name_uz']
        db_table = 'damage'


class Sprayer(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Опрыскиватель'
        ordering = ['name_uz']
        db_table = 'sprayer'


class ProtectiveClothing(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = IsActiveManager()

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Индивидуальные средства защиты'
        ordering = ['name_uz']
        db_table = 'protective_clothing'


class EmptyContainersStatus(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Пустые контейнеры'
        ordering = ['name_uz']
        db_table = 'empty_containers_status'


class SprayMonitoringAct(models.Model):
    number = models.CharField(max_length=11, null=True, blank=True)
    given_date = models.DateField(null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    territory_name = models.CharField(max_length=256, verbose_name='Hudud yoki fermer xojalik nomi')
    geometry = models.MultiPointField()
    fumigator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='spray_monitoring_acts')
    infested_area_in_ha = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Tarqalgan maydon')
    treated_area_in_ha = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Ishlangan maydon')
    vegetation_type = models.ForeignKey(VegetationType, on_delete=models.CASCADE, related_name='+', verbose_name='O`simlik qoplami turi')
    vegetation_height_in_sm = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Osimliklar balandligi')
    vegetation_cover = models.ForeignKey(VegetationCover, on_delete=models.CASCADE, related_name='+')
    damage_level = models.ForeignKey(DamageLevel, on_delete=models.CASCADE, related_name='+', verbose_name='Zararlanish darajasi')
    damaged_area_in_ha = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='Zararlangan maydon')
    starting_at = models.DateTimeField(verbose_name='Ishlov berish boshlangan vaqt')
    ending_at = models.DateTimeField(verbose_name='Ishlov berish tugallangan vaqt')
    temperature_at_beginning = models.CharField(max_length=8, verbose_name='Ishlov boshlangan davrdaki havo harorati')
    temperature_at_end = models.CharField(max_length=8, verbose_name='Ishlov tugagan davrdaki havo harorati')
    locust = models.ManyToManyField(Locust, related_name='+', verbose_name='Chigirtka turi')
    locust_age = models.ForeignKey(LocustAge, on_delete=models.CASCADE, related_name='+', verbose_name='Lichinka yoshi')
    is_imago = models.BooleanField(default=False, verbose_name='Voyaga yetgan')
    density = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Zichligi')
    bands = models.BooleanField(default=False, verbose_name='Lichinkalar to`dasi')
    swarms = models.BooleanField(default=False, verbose_name='To`dalar')
    scattered = models.BooleanField(default=False, verbose_name='Mayda todalarga ajralish')
    locust_stage = models.ForeignKey(LocustStage, on_delete=models.CASCADE, related_name='+', verbose_name='Rivojlanish bosqichi')
    sprayer = models.ManyToManyField(Sprayer, related_name='+', verbose_name='Purkagich')
    sprayer_model = models.CharField(max_length=128, verbose_name='Purkagich modeli')
    atomizer_height_above_ground_in_m = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Purkashning yer yzuasidan balandligi')
    barriers = models.BooleanField(default=False, verbose_name='Tosiq')
    length_of_barriers_in_m = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='To`siq uzunligi')
    distance_between_barriers_in_m = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='To`siq oraligi')
    average_speed_of_movement_in_km_s = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Harakatnign ortacha tezligi')
    protective_clothing = models.ManyToManyField(ProtectiveClothing, related_name='+', verbose_name='Maxsus himoya vositalari')
    is_clean_protective_clothing = models.BooleanField(default=True, verbose_name='Himoya kiyimi toza va yaxshi holatdami')
    adverse_effect_to_fumigator = models.BooleanField(default=False, verbose_name='Ish bajaruvchi behosdan insektisid tasiriga uchradimi')
    empty_containers_status = models.ManyToManyField(EmptyContainersStatus, related_name='+', verbose_name='Bo`sh kontenyerlar')
    is_effected_on_non_target_organisms = models.BooleanField(default=False, verbose_name='Boshqa organizimlarga tasiri')
    note = models.TextField()
    status = models.IntegerField(choices=SprayMonitoringStatus.choices, default=SprayMonitoringStatus.SAVED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number if self.number else str(self.pk)

    class Meta:
        indexes = [models.Index(fields=['number', ]), models.Index(fields=['given_date', ])]
        verbose_name = 'Противосаранчовые обработки'
        ordering = ['number']
        db_table = 'spray_monitoring_act'


class SpentInsecticide(models.Model):
    spray_monitoring_act = models.ForeignKey(SprayMonitoringAct, on_delete=models.CASCADE, related_name='spent_insecticides')
    insecticide = models.ForeignKey(Insecticide, on_delete=models.CASCADE, related_name='+')
    dose = models.DecimalField(max_digits=7, decimal_places=3)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.insecticide.name_uz

    class Meta:
        db_table = 'spent_insecticide'


class SprayMonitoringActAlbum(models.Model):
    spray_monitoring_act = models.ForeignKey(SprayMonitoringAct, on_delete=models.CASCADE, related_name='album')
    image = models.ImageField(upload_to='spray_monitoring_act/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.url

    class Meta:
        db_table = 'spray_monitoring_act_album'


class SprayMonitoringEfficiency(models.Model):
    spray_monitoring_act = models.ForeignKey(SprayMonitoringAct, on_delete=models.CASCADE, related_name='efficiencies')
    efficiency = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='Ishlovning biologik samaradorligi')
    period_in_hours = models.PositiveSmallIntegerField(verbose_name='Ishlovdan keyin otgan vaqt (soat)')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.efficiency} % {self.period_in_hours} soatdan song'

    class Meta:
        db_table = 'spray_monitoring_efficiency'


class SprayMonitoringEfficiencyAct(models.Model):
    spray_monitoring_act = models.OneToOneField(SprayMonitoringAct, on_delete=models.CASCADE, related_name='efficiency_act')
    number = models.CharField(max_length=11)
    given_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'spray_monitoring_efficiency_act'
