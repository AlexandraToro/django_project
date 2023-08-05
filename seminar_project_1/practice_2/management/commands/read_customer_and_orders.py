from django.core.management.base import BaseCommand
from ...models import Client,Order


class Command(BaseCommand):
	help = "show all orders by customer ID"
	
	def add_arguments(self, parser):
		parser.add_argument('pk', type=int, help='ID of client')
	
	def handle(self, *args, **kwargs):
		pk = kwargs.get('pk')
		if client := Client.objects.filter(pk=pk).first():
			if orders := Order.objects.filter(customer=client).all():
				self.stdout.write(f'List of orders:\n{orders}')
			else:
				self.stdout.write(f'Order of {client} not found')
		else:
			self.stdout.write(f'Client with id = {pk} not found')