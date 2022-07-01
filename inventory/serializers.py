from rest_framework import serializers
from .models import Product, ProductInventory, Brand, ProductAttributeValue, Media


class AllProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class ProductAttributeValues(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        exclude = ['id']
        depth = 2


class MediaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ['image', 'alt_text']

    def get_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)


class ProductInventorySerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    attribute = ProductAttributeValues(source='attribute_values', many=True)
    image = MediaSerializer(source='media_product_inventory', many=True)

    class Meta:
        model = ProductInventory
        fields = [
            'sku',
            'image',
            'store_price',
            'is_default',
            'product',
            'product_type',
            'brand',
            'attribute'
        ]
        read_only = True
        # depth = 3
