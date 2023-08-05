from django.core.management.base import BaseCommand
from ...models import Product


class Command(BaseCommand):
	help = "delete product by ID"
	
	def add_arguments(self, parser):
		parser.add_argument('pk', type=int, help='ID of article')
	
	def handle(self, *args, **kwargs):
		pk = kwargs.get('pk')
		product = Product.objects.filter(pk=pk).first()
		product.delete()
		self.stdout.write(f'Deleted: {product}')
