from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from shop.models import Category, Product
from shop.serializers import CategorySerializer, ProductSerializer, ProductCreateUpdateSerializer

# 5.CREATE VIEWs / VIEWSETs

#  FOR CATEGORIES:


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# FOR PRODUCTS:


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer(self, *args, **kwargs):
        if self.action in ["create","update"]:
            return ProductCreateUpdateSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        category = self.request.query_params.get('category')
        if category:
            self.queryset = self.queryset.filter(category_name=category)
            return self.queryset
        return super().get_queryset(*args, **kwargs)

