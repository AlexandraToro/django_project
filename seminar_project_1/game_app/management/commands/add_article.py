from random import randint

from django.core.management.base import BaseCommand
from ...models import Author, Article
from datetime import datetime


class Command(BaseCommand):
	help = "add new article"
	
	def add_arguments(self, parser):
		parser.add_argument('amount', type=int, help='amount of fake data')
	
	def handle(self, *args, **kwargs):
		amount = kwargs.get('amount')
		for i in range(1, amount + 1):
			author = Author(
				name=f"Author Name{i}",
				surname=f"Author SurName{i}",
				email=f'mail{i}@mail.ru',
				biography=f'{"biography" * i}',
				birthday=datetime.today()
			)
			author.save()
			for j in range(1, amount + 1):
				article = Article(
					title=f"Title {j}{i}",
					content='Lorem ipsum' * j * amount,
					author=author,
					category=f'{randint(1, 5)}',
				)
				article.save()
