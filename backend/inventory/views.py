from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import InventoryBalance
from .serializers import InventoryBalanceSerializer


class InventoryLowStockAPIView(APIView):
    def get(self, request):
        queryset = InventoryBalance.objects.select_related('product').filter(
            quantity_on_hand__lte=F('product__min_stock'),
        )
        serializer = InventoryBalanceSerializer(queryset, many=True)
        return Response(serializer.data)


class InventoryForecastCriticalAPIView(APIView):
    def get(self, request):
        return Response([])
