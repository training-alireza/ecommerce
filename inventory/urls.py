from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "demo"


router = routers.DefaultRouter()
router.register(
    r'all-products', views.AllProductViewSet, basename='all-products',
)
router.register(
    r'api/product', views.ProductInventoryViewSet, basename='product'
)

urlpatterns = [
    # path('', views.home, name='home'),
    path('categories/', views.category, name='categories'),
    path('product-by-category/<str:category>/', views.product_by_category, name='product_by_category'),
    path('product-detail/<str:slug>', views.product_detail, name='product_detail'),

    path('', include(router.urls))
]
