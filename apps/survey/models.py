# from django.db import models
from django.conf import settings
from django.contrib.gis.db import models

from common.models import District
from survey.choices import SurveyStatus


class Biotope(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Биотоп'
        ordering = ['name_uz']
        db_table = 'biotope'


class Vegetation(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Растительность'
        ordering = ['name_uz']
        db_table = 'vegetation'


class VegetationCover(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Густота растительного покрова'
        ordering = ['name_uz']
        db_table = 'vegetation_cover'


class Locust(models.Model):
    alpha_code = models.CharField(max_length=8, unique=True)
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    description_uz = models.TextField()
    description_en = models.TextField()
    description_ru = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Саранча'
        ordering = ['name_uz']
        db_table = 'locust'


class LocustAlbum(models.Model):
    locust = models.ForeignKey(Locust, related_name='album', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='locust/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Альбом саранчи'
        db_table = 'locust_album'


class LocustStage(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Фаза'
        ordering = ['name_uz']
        db_table = 'locust_stage'


class LocustAge(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Возраст личинок'
        ordering = ['name_uz']
        db_table = 'locust_age'


class LocustAppearance(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Присутствуют Саранчовые'
        ordering = ['name_uz']
        db_table = 'locust_appearance'


class NaturalEnemy(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Естественные враги'
        ordering = ['name_uz']
        db_table = 'natural_enemy'


class EggHatching(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Отрождение'
        ordering = ['name_uz']
        db_table = 'egg_hatching'


class Behaviour(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Поведение'
        ordering = ['name_uz']
        db_table = 'behaviour'


class Fledging(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Окрыление'
        ordering = ['name_uz']
        db_table = 'fledging'


class SwarmDensity(models.Model):
    name_uz = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    name_ru = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Плотность в стае'
        ordering = ['name_uz']
        db_table = 'swarm_density'


class Survey(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='surveys')
    territory_name = models.CharField(max_length=256, verbose_name='Hudud yoki fermer xojalik nomi')
    geometry = models.MultiPointField()
    agronomist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='surveys', verbose_name='Tekshiruvchi guruh rahbarining ismi')
    surveyed_area_in_ha = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Tekshirilgan maydon(ga)')
    biotope = models.ForeignKey(Biotope, on_delete=models.CASCADE, related_name='+', verbose_name='Biotop turi')
    vegetation = models.ForeignKey(Vegetation, on_delete=models.CASCADE, related_name='+', verbose_name='Osimliklar')
    vegetation_cover = models.ForeignKey(VegetationCover, on_delete=models.CASCADE, related_name='+', verbose_name='Otlarning qalinligi')
    temperature = models.CharField(max_length=8, verbose_name='Havo harorati')
    wind = models.CharField(max_length=8, verbose_name='Shamol')
    locust_appearance = models.ManyToManyField(LocustAppearance, related_name='+', verbose_name='Chigirtkaning mavjudligi')
    locusts = models.ManyToManyField(Locust, related_name='+')
    damaged_area_in_ha = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Tarqalgan maydoni')
    note = models.TextField()
    status = models.IntegerField(choices=SurveyStatus.choices, default=SurveyStatus.SAVED)
    approved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.territory_name

    class Meta:
        indexes = [models.Index(fields=['approved_at', ]), ]
        verbose_name = 'Обследования саранчи'
        db_table = 'survey'


class SurveyAlbum(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='album')
    image = models.ImageField(upload_to='survey/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.url

    class Meta:
        db_table = 'survey_album'


class LocustAppearanceDetailInfo(models.Model):
    survey = models.OneToOneField(Survey, on_delete=models.CASCADE, related_name='locust_appearance_detail_info')
    egg_pod_detected_area = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='Kozacha joylashgan maydon')
    egg_pod_density_from = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Kozacha zichligi(ta/m2) dan')
    egg_pod_density_to = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Kozacha zichligi(ta/m2) gacha')
    average_number_of_eggs_in_pod = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Kozachadagi tuxumlar soni(ortacha)')
    viability_of_eggs = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Tuxumning hayotchanligi')
    natural_enemies = models.ManyToManyField(NaturalEnemy, blank=True, related_name='+', verbose_name='Tabiiy kushandalarning borligi')
    egg_hatching = models.ForeignKey(EggHatching, on_delete=models.CASCADE, related_name='+', null=True, blank=True, verbose_name='Tuxumdan chiqishi')
    hopper_age = models.ForeignKey(LocustAge, on_delete=models.CASCADE, related_name='+', null=True, blank=True, verbose_name='Lichinkalar yoshi')
    hopper_stage = models.ForeignKey(LocustStage, on_delete=models.CASCADE, related_name='+', null=True, blank=True, verbose_name='Rivojlanish bosqichi')
    hopper_density_from = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Lichinkalar zichligi(ta/m2) dan')
    hopper_density_to = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Lichinkalar zichligi(ta/m2) dan')
    min_density_in_hopper_band = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Todadagi lichinkalarning minimal miqdori(ta/m2)')
    max_density_in_hopper_band = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Todadagi lichinkalarning maximal miqdori(ta/m2)')
    area_of_hopper_bands_in_m2 = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True, verbose_name='Toda tarqalgan yerning maydoni(m2)')
    behaviour = models.ForeignKey(Behaviour, on_delete=models.CASCADE, related_name='+', null=True, blank=True, verbose_name='Hatti-harakati')
    hopper_age_in_band = models.ForeignKey(LocustAge, on_delete=models.CASCADE, related_name='+', null=True, blank=True, verbose_name='Lichikalar yoshi')
    adult_fledging = models.ForeignKey(Fledging, on_delete=models.CASCADE, related_name='+', null=True, blank=True, verbose_name='Qanot chiqarish')
    adult_maturity = models.BooleanField(null=True, blank=True, verbose_name='Urchishga tayyorligi')
    adult_stage = models.ForeignKey(LocustStage, on_delete=models.CASCADE, related_name='+', null=True, blank=True, verbose_name='Rivojlanish bosqichi')
    adult_feeding_and_roosting = models.BooleanField(null=True, blank=True, verbose_name='Oziqlanish va osimliklarda ornashishi')
    adult_copulating = models.BooleanField(null=True, blank=True, verbose_name='Urchishi va juftlashishi')
    adult_laying = models.BooleanField(null=True, blank=True, verbose_name='Tuxum quyishi')
    adult_flying = models.BooleanField(null=True, blank=True, verbose_name='Uchishi')
    swarm_maturity = models.BooleanField(null=True, blank=True, verbose_name='Urchisga tayyorligi')
    swarm_density = models.ForeignKey(SwarmDensity, on_delete=models.CASCADE, related_name='+', null=True, blank=True, verbose_name='Todalarning zichligi')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.survey.territory_name

    class Meta:
        db_table = 'locust_appearance_detail_info'


class SurveyAct(models.Model):
    survey = models.OneToOneField(Survey, on_delete=models.CASCADE, related_name='act')
    number = models.CharField(max_length=11)
    given_date = models.DateField(auto_now_add=True)
    agronomist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='survey_acts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Акт Обследования саранчи'
        indexes = [models.Index(fields=['number', ]), models.Index(fields=['given_date', ])]
        ordering = ['number']
        db_table = 'survey_act'


