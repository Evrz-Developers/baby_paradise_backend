from django.contrib import admin
from shop.models import Product, Category

# 3. REGISTER THE MODELS
admin.site.register(Product)
admin.site.register(Category)
