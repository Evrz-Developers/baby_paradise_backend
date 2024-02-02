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

    def create(self, validated_data):
        # Check if 'item_code' is provided before creating the instance
        item_code = validated_data.get('item_code')
        if item_code:
            print("Item code checked!")
            # Check if an existing product with the same 'item_code' exists
            existing_product = Product.objects.filter(
                item_code=item_code).first()
            if existing_product:
                # Handle the case where the 'item_code' is not unique
                print("Item code is not unique!")
                raise serializers.ValidationError(
                    {'item_code': 'Item code must be unique.'})

        return super().create(validated_data)
