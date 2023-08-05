from django.core.management.base import BaseCommand
from ...models import Order


class Command(BaseCommand):
	help = "show all orders"
	
	def handle(self, *args, **kwargs):
		order = Order.objects.all()
		self.stdout.write(f'All orders:\n {order}')
