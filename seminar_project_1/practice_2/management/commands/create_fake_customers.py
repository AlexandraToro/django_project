from datetime import datetime

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Client

fake = Faker('ru_RU')


class Command(BaseCommand):
	help = "create fake customers"
	
	def add_arguments(self, parser):
		parser.add_argument('count', type=int, help="Count of fake customers")
	
	def handle(self, *args, **kwargs):
		c = kwargs.get('count')
		for i in range(1, c + 1):
			client = Client(
				name=fake.name(),
				email=fake.ascii_email(),
				phone=fake.phone_number(),
				address=fake.address(),
				reg_time=fake.date_between()
			)
			client.save()
		self.stdout.write(f"Created {c} customers")