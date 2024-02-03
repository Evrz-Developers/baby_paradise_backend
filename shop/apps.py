from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
    
    def ready(self):
        from django.contrib import admin
        admin.site.site_header = 'Margin Point Admin'
