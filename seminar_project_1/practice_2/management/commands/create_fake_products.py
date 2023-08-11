from datetime import datetime
from random import randint

from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Product

fake = Faker('ru_RU')


class Command(BaseCommand):
	help = "create fake customers"
	
	def add_arguments(self, parser):
		parser.add_argument('count', type=int, help="Count of fake customers")
	
	def handle(self, *args, **kwargs):
		c = kwargs.get('count')
		for i in range(1, c + 1):
			client = Product(
				name=f'Name of product {i}',
				description=fake.text(max_nb_chars=50),
				price=randint(1, 100000),
				count=randint(1, 10),
				add_time=datetime.now()
			)
			client.save()
		self.stdout.write(f"Created {c} products")
