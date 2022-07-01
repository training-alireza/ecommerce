from django.contrib import admin

from .models import Category, Product, ProductInventory, ProductType, Brand, Stock, ProductAttribute, \
    ProductAttributeValues, ProductAttributeValue, ProductTypeAttribute, Media


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductTypeAttribute)
class ProductTypeAttributeAdmin(admin.ModelAdmin):
    pass


class BookInline(admin.TabularInline):
    model = ProductTypeAttribute


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]


class ProductTypeInline(admin.TabularInline):
    model = ProductType


class MediaInline(admin.TabularInline):
    model = Media


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    pass
    inlines = [
        MediaInline
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAttributeValues)
class ProductAttributeValuesAdmin(admin.ModelAdmin):
    pass
