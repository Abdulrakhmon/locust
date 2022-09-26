from django.contrib import admin

from spray_monitoring.models import ActiveSubstance, Formulation, Insecticide, InsecticidesYearlyRemainder, Sprayer, \
    ProtectiveClothing, EmptyContainersStatus, SprayMonitoringAct, SpentInsecticide, DamageLevel, VegetationType, \
    SprayMonitoringActAlbum, InsecticideExchange, SprayMonitoringEfficiency, SprayMonitoringEfficiencyAct


@admin.register(ActiveSubstance)
class ActiveSubstanceAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Formulation)
class FormulationAdmin(admin.ModelAdmin):
    list_display = ['alpha_code_uz', 'alpha_code_en', 'alpha_code_ru', 'name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Insecticide)
class InsecticideAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'is_active', 'created_at', 'updated_at']
    search_fields = ['name_en']
    list_filter = ['is_active']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(InsecticideExchange)
class InsecticideExchangeAdmin(admin.ModelAdmin):
    list_display = ['insecticide', 'amount',  'given_date', 'sender_region', 'receiver_region', 'created_at', 'updated_at']
    search_fields = ['amount']
    list_filter = ['sender_region', 'receiver_region']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(InsecticidesYearlyRemainder)
class InsecticidesYearlyRemainderAdmin(admin.ModelAdmin):
    list_display = ['insecticide', 'amount',  'year', 'created_at', 'updated_at']
    search_fields = ['name_en']
    list_filter = ['region', ]

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Sprayer)
class SprayerAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(ProtectiveClothing)
class ProtectiveClothingAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'is_active', 'created_at', 'updated_at']
    search_fields = ['name_en']
    list_filter = ['is_active']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(EmptyContainersStatus)
class EmptyContainersStatusAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(DamageLevel)
class DamageLevelAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(VegetationType)
class VegetationTypeAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False


class SprayMonitoringActAlbumInline(admin.TabularInline):
    extra = 0
    model = SprayMonitoringActAlbum


class SpentInsecticideInline(admin.TabularInline):
    extra = 0
    model = SpentInsecticide


class SprayMonitoringEfficiencyInline(admin.TabularInline):
    extra = 0
    model = SprayMonitoringEfficiency
    readonly_fields = ['efficiency', 'period_in_hours', 'created_at', 'updated_at']


class SprayMonitoringEfficiencyActInline(admin.TabularInline):
    extra = 0
    model = SprayMonitoringEfficiencyAct
    readonly_fields = ['number', 'given_date', 'created_at', 'updated_at']


@admin.register(SprayMonitoringAct)
class SprayMonitoringActAdmin(admin.ModelAdmin):
    inlines = [SprayMonitoringActAlbumInline, SpentInsecticideInline, SprayMonitoringEfficiencyInline, SprayMonitoringEfficiencyActInline]
    list_display = ['number', 'given_date', 'fumigator', 'created_at', 'updated_at']
    search_fields = ['number']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(SprayMonitoringEfficiencyAct)
class SprayMonitoringEfficiencyActAdmin(admin.ModelAdmin):
    list_display = ['number', 'given_date', 'created_at', 'updated_at']
    search_fields = ['spray_monitoring_act__number', 'number']

    # def has_delete_permission(self, request, obj=None):
    #     return False
