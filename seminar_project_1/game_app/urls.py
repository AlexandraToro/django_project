from django.urls import path
from . import views

urlpatterns = [
	path('coinplay/<int:count>', views.coin, name='coin'),
	path('cube/<int:count>', views.dice, name='cube'),
	path('r_n/<int:count>', views.rand_int, name='random_number'),
	path('articles/<int:pk>', views.get_articles_by_author, name='articles'),
	path('article/<int:pk>', views.article, name='article'),
]
