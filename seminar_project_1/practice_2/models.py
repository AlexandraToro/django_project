from django.db import models


class Client(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=13)
	address = models.CharField(max_length=200)
	reg_time = models.DateField()
	
	def __str__(self):
		return f'{self.name}'


class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=8, decimal_places=2)
	count = models.IntegerField()
	add_time = models.DateField(auto_now_add=True)
	image = models.ImageField(default=None, null=True)
	
	def __str__(self):
		return f'Product: {self.name}, price {self.price}'


class Order(models.Model):
	customer: Client = models.ForeignKey(Client, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product)
	total_sum = models.DecimalField(max_digits=8, decimal_places=2)
	order_date = models.DateField(auto_now_add=True)
	
	def __str__(self):
		return f'\nCustomer: {self.customer},' \
		       f'Email: {self.customer.email}, \n' \
		       f'total sum of order {self.total_sum}'
