from django.contrib import admin
from shop.models import Product, Category, Document
from django.utils.translation import ngettext
from django.contrib import messages

# 3. REGISTER THE MODELS


class ProductAdmin(admin.ModelAdmin):
    actions = ['duplicate_selected']

    def duplicate_selected(self, request, queryset):
        for product in queryset:
            # Clear primary key to create a new instance
            product.pk = None
            product.item_code = None
            product.save()

        self.message_user(
            request,
            ngettext(
                'Successfully duplicated %(count)d product.',
                'Successfully duplicated %(count)d products.',
                queryset.count(),
            ) % {'count': queryset.count()},
            messages.SUCCESS,
        )

    duplicate_selected.short_description = "Duplicate selected products"


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Document)
