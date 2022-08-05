from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from common.models import User, Country, Region, District, Unit


class CustomUserAdmin(UserAdmin):
    change_user_password_template = None
    model = User
    list_display = ['name_uz', 'name_en', 'name_ru', 'phone', 'pin', 'passport_series_and_number', 'created_at', 'last_login']
    list_filter = ['region', 'status']
    search_fields = ['username', 'pin']
    filter_vertical = []
    filter_horizontal = []
    fieldsets = [
        [
            "Authentication",
            {
                'fields': [
                    'username',
                    'password',
                ]
            }
        ],
        [
            "Details",
            {
                'fields': [
                    'name_uz',
                    'name_en',
                    'name_ru',
                    'pin',
                    'passport_series_and_number',
                    'phone',
                    'region',
                    'districts',
                    'status',
                ]
            }
        ],
        [
            'Authorization',
            {
                'fields': [
                    'groups',
                    'user_permissions',
                    'is_staff',
                    'is_superuser',
                ]
            }
        ],
    ]
    add_fieldsets = [
        [
            "Authentication",
            {
                'fields': [
                    'username',
                    'password1',
                    'password2',
                ],
            }
        ],
        [
            "Details",
            {
                'classes': ['wide'],
                'fields': [
                    'name_uz',
                    'name_en',
                    'name_ru',
                    'pin',
                    'passport_series_and_number',
                    'phone',
                    'region',
                    'districts',
                    'status',
                ],
            }
        ],
        [
            'Authorization',
            {
                'fields': [
                    'groups',
                ]
            }
        ]
    ]

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(User, CustomUserAdmin)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'alpha_two_code', 'alpha_three_code', 'created_at', 'updated_at']
    search_fields = ['name_en', 'alpha_two_code', 'alpha_three_code']

    # def has_delete_permission(self, request, obj=None):
    #     return False@admin.register(Country)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']
    list_filter = ['country']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']
    list_filter = ['region']

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'created_at', 'updated_at']
    search_fields = ['name_en']

    # def has_delete_permission(self, request, obj=None):
    #     return False
