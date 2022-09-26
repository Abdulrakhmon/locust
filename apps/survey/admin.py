from django.contrib import admin

from survey.models import Biotope, Vegetation, VegetationCover, Locust, LocustAlbum, LocustStage, LocustAge, \
    LocustAppearance, NaturalEnemy, EggHatching, Behaviour, Fledging, Survey, SurveyAlbum, LocustAppearanceDetailInfo, \
    SurveyAct, SwarmDensity


@admin.register(Biotope)
class BiotopeAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Vegetation)
class VegetationAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(VegetationCover)
class VegetationCoverAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


class LocustAlbumInline(admin.TabularInline):
    extra = 0
    model = LocustAlbum


@admin.register(Locust)
class LocustAdmin(admin.ModelAdmin):
    inlines = [LocustAlbumInline]
    list_display = ['alpha_code', 'name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(LocustStage)
class LocustStageAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(LocustAge)
class LocustAgeAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(LocustAppearance)
class LocustAppearanceAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(NaturalEnemy)
class NaturalEnemyAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(EggHatching)
class EggHatchingAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Behaviour)
class BehaviourAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Fledging)
class FledgingAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(SwarmDensity)
class SwarmDensityAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


class SurveyAlbumInline(admin.TabularInline):
    extra = 0
    model = SurveyAlbum


class LocustAppearanceDetailInfoInline(admin.TabularInline):
    extra = 0
    model = LocustAppearanceDetailInfo


class SurveyActInline(admin.TabularInline):
    extra = 0
    model = SurveyAct
    readonly_fields = ['number', 'given_date', 'agronomist']


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    inlines = [SurveyAlbumInline, LocustAppearanceDetailInfoInline, SurveyActInline]
    list_display = ['territory_name', 'agronomist', 'status', 'created_at', 'updated_at']
    search_fields = ['territory_name']

    # def has_delete_permission(self, request, obj=None):
    #     return False
