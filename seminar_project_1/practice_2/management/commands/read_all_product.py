from django.core.management.base import BaseCommand
from ...models import Product


class Command(BaseCommand):
	help = "show all products"
	
	def handle(self, *args, **kwargs):
		products = Product.objects.all()
		self.stdout.write(f'All products:\n {products}')
