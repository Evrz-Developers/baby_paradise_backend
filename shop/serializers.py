# 4. CREATE SERIALIZERS
# Serializers define the API representation.
from rest_framework import serializers
from shop.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def validate_item_code(self, value):
        # Treat empty string as None
        if not value:
            return None

        # Check if 'item_code' is unique if provided
        existing_product = Product.objects.filter(item_code=value).first()
        if existing_product:
            raise serializers.ValidationError(
                {'item_code': 'Item code must be unique.'})

        return value

    def create(self, validated_data):
        return super().create(validated_data)


class ProductListByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['category']
