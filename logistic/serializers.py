from dataclasses import fields
from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # налаштуйте серіалізатор для продукту
    class Meta:
        model = Product
        fields = ['id', 'title', 'description',]

 
class ProductPositionSerializer(serializers.ModelSerializer):
    # налаштуйте серіалізатор для позиції продукту на складі
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # налаштуйте серіалізатор для складу

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions', ]

    def create(self, validated_data):
        # витягуємо пов'язані дані для інших таблиць
        positions = validated_data.pop('positions')

        # створюємо склад за його параметрами
        stock = super().create(validated_data)

        # тут вам треба заповнити пов'язані таблиці
        # у нашому випадку: таблицю StockProduct
        # за допомогою списку positions

        for pos in positions:
            StockProduct.objects.create(stock=stock, **pos)

        return stock

    def update(self, instance, validated_data):
        # витягуємо пов'язані дані для інших таблиць
        positions = validated_data.pop('positions')

        # оновлюємо склад за його параметрами
        stock = super().update(instance, validated_data)

        # тут вам треба оновити пов'язані таблиці
        # у нашому випадку: таблицю StockProduct
        # за допомогою списку positions

        for pos in positions:
                  
            obj, created = StockProduct.objects.update_or_create(
                    stock=stock, 
                    product=pos.get('product'),
                    defaults={
                        'quantity': pos.get('quantity'), 
                        'price': pos.get('price'), 
                    },
                )

        return stock
