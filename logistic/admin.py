from django.contrib import admin
from logistic.models import Product, Stock, StockProduct

# Register your models here.

class StockInline(admin.TabularInline):
    model = Stock.products.through
    extra = 1

class ProductInline(admin.TabularInline):
    model = Product.stocks.through
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['id', 'title']
    inlines = [StockInline,]

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    list_display_links = ['id', 'address']
    list_filter = ['id', 'address']
    search_fields = ['products__title']
    inlines = [ProductInline,]

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ['stock', 'product', 'quantity', 'price']

# Зміни для заміни картинки Django Admin
admin.site.site_header = 'Warehouse logistics'
admin.site.site_title = 'WL'
admin.site.index_title = 'Administrator panel'
