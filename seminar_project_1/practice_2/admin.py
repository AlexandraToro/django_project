from django.contrib import admin
from .models import Product, Order, Client


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'count']
	ordering = ['-price']
	list_filter = ['add_time', 'price']
	search_fields = ['description']
	search_help_text = 'Поиск по полю Описание продукта	(description)'


class ClientAdmin(admin.ModelAdmin):
	list_display = ['name']
	ordering = ['name']
	list_filter = ['address']
	fields = ['name', 'email', 'address', 'phone', 'reg_time']
	readonly_fields = ['reg_time']


class OrderAdmin(admin.ModelAdmin):
	list_display = ['customer', 'order_date', 'total_sum']
	ordering = ['order_date', '-total_sum']
	list_filter = ['order_date']
	readonly_fields = ['customer', 'products', 'total_sum', 'order_date']


admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
