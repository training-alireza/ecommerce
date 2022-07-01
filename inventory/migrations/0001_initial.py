# Generated by Django 4.0.5 on 2022-06-30 18:53

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='category name')),
                ('slug', models.SlugField(max_length=150, verbose_name='category safe url')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='inventory.category', verbose_name='parent of category')),
            ],
            options={
                'verbose_name': 'product category',
                'verbose_name_plural': 'product categories',
            },
        ),
    ]