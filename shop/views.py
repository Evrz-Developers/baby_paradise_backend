from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from shop.models import Category, Product, Document
from shop.serializers import CategorySerializer, ProductSerializer, ProductCreateUpdateSerializer, ProductListByCategorySerializer, DocumentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny


# CREATE VIEWs / VIEWSETs

#  FOR CATEGORIES:
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


# FOR PRODUCTS:
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return ProductCreateUpdateSerializer
        elif self.action == 'list' and self.request.query_params.get('category'):
            return ProductListByCategorySerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class ProductsByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = get_object_or_404(Category, pk=category_id)
        return Product.objects.filter(category=category)


class DocumentDownloadView(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        name = self.kwargs.get('name')
        return get_object_or_404(Document, name=name)
