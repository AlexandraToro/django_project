from django.core.management.base import BaseCommand
from ...models import Product, Client, Order


class Command(BaseCommand):
	help = "create fake customers"
	
	def add_arguments(self, parser):
		parser.add_argument('pk', type=int, help="Customer ID")
		parser.add_argument('pk_prod', type=int, help="List of set(Product ID, Product quantity)")
		parser.add_argument('count', type=int, help="Product quantity")
	
	def handle(self, *args, **kwargs):
		pk = kwargs.get('pk')
		prod_pk = kwargs.get('pk_prod')
		count = kwargs.get('count')
		client = Client.objects.filter(pk=pk).first()
		product = Product.objects.filter(pk=prod_pk).first()
		sum = product.price * count
		order = Order(
			customer=client,
			total_sum=sum,
		)
		order.save()
		for i in range(count):
			order.products.add(product)
		order.save()
		
		self.stdout.write(f"Created order")
