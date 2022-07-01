from django.db.models import Count
from django.shortcuts import render
from .models import Category, Product, ProductInventory
from django.shortcuts import get_object_or_404


# Create your views here.


def home(request):
    return render(request, 'base.html')


def category(request):
    objects = Category.objects.all()
    return render(request, 'categories.html', {'data': objects})


def product_by_category(request, category):
    data = Product.objects.filter(category__slug=category).values(
        'id', 'name', 'slug', 'category__name', 'product__store_price')
    return render(request, 'product_by_category.html', {'data': data})


# def product_detail(request, slug):
#
#     filter_arguments = []
#     if request.GET:
#         for value in request.GET.values():
#             filter_arguments.append(value)
#
#     data = ProductInventory.objects.filter(product__slug=slug).filter(is_default=True)\
#         .values("id", "sku", "product__name", "store_price", "product_inventory__unit")
#     return render(request, 'product_detail.html', {'data': data})


def product_detail(request, slug):
    filter_arguments = []
    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)

    data = ProductInventory.objects.filter(product__slug=slug)\
        .filter(attribute_values__attribute_value__in=filter_arguments)\
        .annotate(num_tag=Count('attribute_values'))\
        .filter(num_tag=len(filter_arguments))\
        .values("id", "sku", "product__name", "store_price", "product_inventory__unit")
    print(data)
    return render(request, 'product_detail.html', {'data': data})
