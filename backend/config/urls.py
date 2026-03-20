from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/inventory/', include('inventory.urls')),
]
