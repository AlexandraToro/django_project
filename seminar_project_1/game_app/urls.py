from django.urls import path
from . import views

urlpatterns = [
	path('coinplay/', views.coin, name='index'),
	path('cube/', views.dice, name='index'),
	path('random/', views.rand_int, name='index'),
]
