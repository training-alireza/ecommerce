# Generated by Django 4.0.5 on 2022-06-30 21:20

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='brand name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_id', models.CharField(max_length=50, unique=True, verbose_name='product website id')),
                ('name', models.CharField(max_length=255, verbose_name='product name')),
                ('slug', models.CharField(max_length=255, verbose_name='product safe url')),
                ('description', models.TextField(verbose_name='product description')),
                ('is_active', models.BooleanField(default=True, verbose_name='product visibility')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date product created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date product last updated')),
                ('category', mptt.fields.TreeManyToManyField(to='inventory.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='product attribute name')),
                ('description', models.TextField(verbose_name='product attribute description')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(max_length=255, verbose_name='attribute value')),
                ('product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_attribute', to='inventory.productattribute')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributeValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributevalues', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attributevaluess', to='inventory.productattributevalue')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=20, unique=True, verbose_name='sku')),
                ('universal_product_code', models.CharField(max_length=12, unique=True, verbose_name='universal product code')),
                ('is_active', models.BooleanField(default=True, verbose_name='product visibility')),
                ('retail_price', models.IntegerField(verbose_name='retail price')),
                ('store_price', models.IntegerField(verbose_name='store price')),
                ('sale_price', models.IntegerField(verbose_name='sale price')),
                ('weight', models.FloatField(verbose_name='product weight')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('attribute_values', models.ManyToManyField(related_name='product_attribute_values', through='inventory.ProductAttributeValues', to='inventory.productattributevalue')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Brand', to='inventory.brand')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='inventory.product')),
            ],
            options={
                'verbose_name': 'product inventory',
                'verbose_name_plural': 'products inventory',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_checked', models.DateTimeField(verbose_name='inventory stock check date')),
                ('unit', models.IntegerField(default=0, verbose_name='units/qty of stock')),
                ('product_inventory', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='product_inventory', to='inventory.productinventory')),
            ],
        ),
        migrations.AddField(
            model_name='productinventory',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_type', to='inventory.producttype'),
        ),
        migrations.AddField(
            model_name='productattributevalues',
            name='productinventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productattributevaluess', to='inventory.productinventory'),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', upload_to='images/', verbose_name='product image')),
                ('alt_text', models.CharField(max_length=255, verbose_name='alternative text')),
                ('is_feature', models.BooleanField(default=False, verbose_name='product default image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('product_inventory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='media_product_inventory', to='inventory.productinventory')),
            ],
            options={
                'verbose_name': 'product image',
                'verbose_name_plural': 'product images',
            },
        ),
        migrations.AlterUniqueTogether(
            name='productattributevalues',
            unique_together={('attributevalues', 'productinventory')},
        ),
    ]
