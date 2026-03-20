from django.urls import path

from .views import InventoryForecastCriticalAPIView, InventoryLowStockAPIView

urlpatterns = [
    path('low-stock/', InventoryLowStockAPIView.as_view(), name='inventory-low-stock'),
    path('forecast/critical/', InventoryForecastCriticalAPIView.as_view(), name='inventory-forecast-critical'),
]
