from django.urls import path
from . import views

urlpatterns = [
	path('orders/<int:pk_client>', views.all_orders_by_client, name='all_orders_by_client'),
	path('orders/<int:pk_client>/<str:period>', views.products_by_period, name='products_by_period'),
]