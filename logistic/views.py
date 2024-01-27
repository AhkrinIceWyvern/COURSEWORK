from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # за необхідності додайте параметри фільтрації
    filter_backends = [SearchFilter, ]
    filterset_fields = ['title', 'description',]
    search_fields = ['title', 'description',]
    pagination_class = LimitOffsetPagination 
    


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # за необхідності додайте параметри фільтрації
    filter_backends = [SearchFilter, DjangoFilterBackend,]
    filterset_fields = ['products',]
    search_fields = ['address', 'products__title']
    pagination_class = LimitOffsetPagination 
