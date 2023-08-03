from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('type/', views.type_of_bike, name='type_of_bike')
]
