from django.urls import path
from . import views

urlpatterns = [
	path('coinplay/<int:count>', views.coin, name='coin'),
	path('cube/<int:count>', views.dice, name='cube'),
	path('r_n/<int:count>', views.rand_int, name='random_number'),
	path('articles/<int:pk>', views.get_articles_by_author, name='articles'),
	path('article/<int:pk>', views.article, name='article'),
	path('choose', views.simple_games_forms, name='choose'),
	path('add', views.add_author, name='add_author'),
	path('add_art', views.add_article, name='add_article'),
	path('get_article/<int:article_id>/', views.add_commentary_form_simple, name='add_commentary_form_simple'),
]
