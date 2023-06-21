from django.contrib import admin

from .models import Provider, ProviderUser, License, Configuration

PAGE_ITEMS = 10


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'license_key', 'expire_date', 'created_at')
    search_fields = ['email', 'license_key', 'expire_date']
    list_per_page = PAGE_ITEMS


class ProviderUserAdmin(admin.ModelAdmin):
    list_display = ('provider_id', 'user_id', 'api_key', 'secret_key', 'wallet_amount', 'created_at')
    search_fields = ['api_key', 'secret_key']
    list_per_page = PAGE_ITEMS


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('provider_user_id',
                    'leverage',
                    'interval',
                    'margin_type',
                    'volume_usdt',
                    'amount_usdt',
                    'candle_change_ratio',
                    'profit_percentage',
                    'max_position_count',
                    'is_bollinger_active',
                    'check_position_mode',
                    'blacklist',
                    'roes',
                    'created_at')
    search_fields = ['leverage',
                     'interval',
                     'margin_type',
                     'volume_usdt',
                     'amount_usdt',
                     'candle_change_ratio',
                     'profit_percentage',
                     'max_position_count',
                     'is_bollinger_active',
                     'check_position_mode',
                     'blacklist',
                     'roes']
    list_per_page = PAGE_ITEMS


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ['name']
    list_per_page = PAGE_ITEMS


admin.site.register(License, LicenseAdmin)
admin.site.register(ProviderUser, ProviderUserAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Provider, ProviderAdmin)
