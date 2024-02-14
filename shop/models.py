from django.db import models
from datetime import datetime, timedelta
from io import BytesIO
from PIL import Image
from django.contrib.auth.models import User

# 2. CREATE MODELS:

# MODEL: CATEGORY


class Category(models.Model):
    name = models.CharField(unique=True, max_length=200,
                            verbose_name='Category name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name

# MODEL: PRODUCT


def get_unique_filename(filename):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f'item_{timestamp}.jpg'


def get_default_created_at():
    now = datetime.now()
    adjusted_time = now + timedelta(hours=5, minutes=30)
    return adjusted_time


def compress(image, output_format='JPEG', quality=60):
    im = Image.open(image)
    max_size = (800, 800)
    im.thumbnail(max_size)
    buffer = BytesIO()
    im.save(buffer, format=output_format, quality=quality)
    buffer.seek(0)
    return buffer


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    description = models.CharField(
        max_length=250, null=True, blank=True, verbose_name='Description')
    item_code = models.CharField(
        max_length=50, verbose_name='Item Code', blank=True, null=True)
    bar_code = models.CharField(max_length=50, blank=True, null=True)
    mrp = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0, verbose_name='MRP')
    retail_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    product_image = models.ImageField(
        upload_to='shop/images/products/', null=True, blank=True)
    category = models.ForeignKey(
        Category, verbose_name='Category', null=True, blank=True, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(
        verbose_name='Quantity', null=True, default=0)
    created_at = models.DateTimeField(default=get_default_created_at)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        constraints = [
            models.UniqueConstraint(
                fields=['item_code'],
                name='unique_non_null_item_code',
                condition=models.Q(item_code__isnull=False),
            )
        ]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        # Check if product_image is not None
        if self.product_image:
            # Compress the image before saving.
            compressed_image = compress(self.product_image)
            self.product_image.save(get_unique_filename(self.product_image.name), compressed_image,
                                    save=False)
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
