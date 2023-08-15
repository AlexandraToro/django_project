from random import randint

from django.shortcuts import render, get_object_or_404
import logging
from .models import Author, Article, Comment
from .forms import ChooseGame, AuthoForms, ArticleForms, AddCommentary

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


def simple_games_forms(request):
	coin_sides = ('obverse', 'reverse')
	if request.method == 'POST':
		form = ChooseGame(request.POST)
		title = ["Coin play", " Dice", " Random number"][int(form.data['a_game'])]
		if form.is_valid():
			c = form.cleaned_data["attempts"]
			if title == "Coin play":
				attempts_pack = [coin_sides[randint(0, 1)] for _ in range(c)]
			elif title == "Dice":
				attempts_pack = [randint(0, 6) for _ in range(c)]
			else:
				attempts_pack = [randint(0, 100) for _ in range(c)]
			logger.info(f" show result of game : {title}")
			return render(request, 'game_app/common_records.html',
			              {
				              "title": title,
				              "attempts": attempts_pack,
			              })
	else:
		form = ChooseGame()
		logger.info("sending gae chooser")
		return render(request, 'game_app/choose_game.html', {'form': form, 'title': 'Choose game'})


def add_author(request):
	if request.method == "POST":
		form = AuthoForms(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			surname = form.cleaned_data['surname']
			email = form.cleaned_data['email']
			biography = form.cleaned_data['biography']
			birthday = form.cleaned_data['birthday']
			logger.info(f' Get data : {name}, {surname}, {biography}, {birthday}, {email}')
	else:
		form = AuthoForms()
	return render(request, 'game_app/add_author.html', {'form': form})


def add_article(request):
	if request.method == "POST":
		form = ArticleForms(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			author = form.cleaned_data['author']
			category = form.cleaned_data['category']
			logger.info(f' Get data : {title}, {content}, {category}, {author}')
			article = Article(title=title,content=content,author=author,category=category			)
			logger.info(f"added article {article}")
			article.save()
	else:
		form = ArticleForms
	return render(request, 'game_app/add_article.html', {'form': form})

def add_commentary_form_simple(request, article_id):
    """form to add a commentary by author"""

    article = get_object_or_404(Article, pk=article_id)
    author = get_object_or_404(Author, pk=article.author.pk)
    article.views += 1
    article.save()
    commentaries = Comment.objects.filter(article=article)
    print(type(commentaries))
    context = {
        'article': article,
        'author': author,
        'commentaries': commentaries,
        'form': AddCommentary(),
        'button': 'Publish',
    }

    if request.method == 'POST':
        form = AddCommentary(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author_pk = form.cleaned_data['author_pk']
            c_author = get_object_or_404(Author, pk=author_pk)
            c_article = get_object_or_404(Article, pk=article_id)
            Comment(
                author=c_author,
                article=c_article,
                text=text,
            ).save()

    return render(request, 'game_app/article.html', context)