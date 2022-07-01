from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    name = models.CharField(_('category name'), max_length=100)
    slug = models.SlugField(_('category safe url'), allow_unicode=True, max_length=150)
    is_active = models.BooleanField(_('is active'), default=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, related_name='children',
                            null=True, blank=True, verbose_name='parent of category')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('product category')
        verbose_name_plural = _('product categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    web_id = models.CharField(_('product website id'), unique=True, max_length=50)
    name = models.CharField(_('product name'), max_length=255)
    slug = models.SlugField(_('product safe url'), allow_unicode=True, max_length=255)
    description = models.TextField(_('product description'))
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(_('product visibility'), default=True)
    created_at = models.DateTimeField(_('date product created'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('date product last updated'), auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    name = models.CharField(_('brand name'), max_length=150, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.name}'


class ProductAttribute(models.Model):
    name = models.CharField(_('product attribute name'), max_length=255, unique=True)
    description = models.TextField(_('product attribute description'))

    def __str__(self):
        return f'{self.name}'


class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(ProductAttribute, related_name='product_attribute', on_delete=models.PROTECT)
    attribute_value = models.CharField(_('attribute value'), max_length=255)

    def __str__(self):
        return f'{self.product_attribute.name}:{self.attribute_value}'


class ProductType(models.Model):
    name = models.CharField(_('name'), max_length=150, unique=True)
    product_type_attributes = models.ManyToManyField(
        ProductAttribute,
        related_name='product_type_attribute',
        through='ProductTypeAttribute'
    )

    def __str__(self):
        return f'{self.name}'


class ProductInventory(models.Model):
    sku = models.CharField(_('sku'), max_length=20, unique=True)
    universal_product_code = models.CharField(_('universal product code'), max_length=12, unique=True)
    product_type = models.ForeignKey(ProductType, related_name="product_type", on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, related_name='Brand', on_delete=models.PROTECT)
    attribute_values = models.ManyToManyField(ProductAttributeValue, related_name='product_attribute_values',
                                              through="ProductAttributeValues")
    is_active = models.BooleanField(_('product visibility'), default=True)
    is_default = models.BooleanField(_('default selection'), default=False)
    retail_price = models.IntegerField(_('retail price'))
    store_price = models.IntegerField(_('store price'))
    sale_price = models.IntegerField(_('sale price'))
    weight = models.FloatField(_('product weight'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True, editable=False)
    update_at = models.DateTimeField(_('update at'), auto_now=True)

    def __str__(self):
        return f'{self.product.name}'

    class Meta:
        verbose_name = _('product inventory')
        verbose_name_plural = _('products inventory')


class Media(models.Model):
    product_inventory = models.ForeignKey(ProductInventory, on_delete=models.PROTECT,
                                          related_name='media_product_inventory')
    image = models.ImageField(_('product image'), upload_to='images/', default='images/default.png')
    alt_text = models.CharField(_('alternative text'), max_length=255)
    is_feature = models.BooleanField(_('product default image'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')


class Stock(models.Model):
    product_inventory = models.OneToOneField(ProductInventory, related_name='product_inventory',
                                             on_delete=models.PROTECT)

    last_checked = models.DateTimeField(_('inventory stock check date'))
    unit = models.IntegerField(_('units/qty of stock'), default=0)


class ProductAttributeValues(models.Model):
    attributevalues = models.ForeignKey(
        "ProductAttributeValue",
        related_name="attributevaluess",
        on_delete=models.PROTECT,
    )
    productinventory = models.ForeignKey(
        ProductInventory,
        related_name="productattributevaluess",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = (("attributevalues", "productinventory"),)


class ProductTypeAttribute(models.Model):
    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name='productattribute',
        on_delete=models.PROTECT
    )
    product_type = models.ForeignKey(
        ProductType,
        related_name='producttype',
        on_delete=models.PROTECT
    )

    class Meta:
        unique_together = (("product_attribute", "product_type"),)
