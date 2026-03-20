from django.urls import path

from .views import ProductImportAPIView, ProductListAPIView, ProductSearchAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('search/', ProductSearchAPIView.as_view(), name='product-search'),
    path('import/', ProductImportAPIView.as_view(), name='product-import'),
]
