from django.db import models

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


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Product name')
    category = models.ForeignKey(
        Category, verbose_name='Category name', null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Price')
    description = models.CharField(
        max_length=250, null=True, blank=True, verbose_name='Description')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return self.name
