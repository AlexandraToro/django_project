from random import randint

from django.shortcuts import render, get_object_or_404
import logging
from .models import Author, Article, Comment

logger = logging.getLogger(__name__)


def coin(request, count):
	my_list = [['avers', 'reverse'][randint(0, 1)] for i in range(count)]
	logger.info(f"coin is done, {my_list}")
	context = {
		'title': 'Coin play',
		'my_list': my_list,
	}
	return render(request, 'game_app/coin.html', context)


def dice(request, count):
	my_list = [randint(1, 6) for _ in range(count)]
	logger.info(f"cibe is done {count} time: {my_list}")
	context = {
		'title': "cube dice",
		'my_list': my_list,
	}
	return render(request, 'game_app/cube.html', context)


def rand_int(request, count):
	my_list = [randint(0, 100) for _ in range(count)]
	logger.info(f"rasndom is done, {rand_int}")
	context = {
		'title': "random number from 0 to 100:",
		'my_list': my_list,
	}
	return render(request, 'game_app/r_n.html', context)


def get_articles_by_author(request, pk):
	author = get_object_or_404(Author, pk=pk)
	article = Article.objects.filter(author=author)
	context = {
		'title': f"Article of author {author}",
		'author': author,
		'articles': article
	}
	return render(request, 'game_app/articles.html', context)


def article(request, pk):
	article = get_object_or_404(Article, pk=pk)
	comments = Comment.objects.filter(article=article)
	context = {
		'title': article.title,
		'article': article,
		'comment': comments,
		'author': article.author,
	}
	return render(request, 'game_app/article.html', context)
