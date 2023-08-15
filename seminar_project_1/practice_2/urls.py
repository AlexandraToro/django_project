from django.urls import path
from . import views

urlpatterns = [
	path('orders/<int:pk_client>', views.all_orders_by_client, name='all_orders_by_client'),
	path('orders/<int:pk_client>/<str:period>', views.products_by_period, name='products_by_period'),
	path('product/<int:product_pk>', views.update_product_data, name='update_product'),
	path('product/add_img/<int:product_pk>', views.add_product_img, name='add_product_img'),
]