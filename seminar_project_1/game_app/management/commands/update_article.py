from django.core.management.base import BaseCommand
from ...models import  Article



class Command(BaseCommand):
	help = "update article by ID"
	
	def add_arguments(self, parser):
		parser.add_argument('pk', type=int, help='ID of article')
	
	def handle(self, *args, **kwargs):
		pk = kwargs.get('pk')
		article = Article.objects.filter(pk=pk).first()
		if article:
			article.publish = True
			article.save()
		self.stdout.write(f'{article}')
		