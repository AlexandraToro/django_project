from django.db import models
from datetime import datetime as dt


class Coin(models.Model):
	throws = []
	side = models.CharField(max_length=10)
	time = models.DateTimeField(auto_now_add=True)
	
	@staticmethod
	def get_throws(amount):
		obverse_cnt = 0
		reverse_cnt = 0
		for i in Coin.throws[-amount:]:
			if i[1] == 'obverse':
				obverse_cnt += 1
			if i[1] == 'reverse':
				reverse_cnt += 1
		return {'obverse': obverse_cnt, 'reverse': reverse_cnt}
	
	@staticmethod
	def add_throws(value):
		sides = ('obverse', 'reverse')
		Coin.throws.append((dt.now(), sides[value]))


class Author(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	biography = models.TextField()
	birthday = models.DateField()
	
	def __str__(self):
		return f'{self.name} {self.surname}'
	
	def full_name(self):
		return f'Name: {self.name} {self.surname}'


class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	time = models.DateField(auto_now_add=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	category = models.CharField(max_length=100)
	views = models.IntegerField(default=0)
	publish = models.BooleanField(default=False)
	
	def __str__(self):
		return f'{self.title} {self.author} {self.publish} \n {self.content}'


class Comment(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	text = models.TextField()
	date_create = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"Comment for article '{self.article.title}';author: {self.author.name} "
