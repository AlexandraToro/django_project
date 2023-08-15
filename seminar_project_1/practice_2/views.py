from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from practice_2.models import Client, Order, Product
from datetime import datetime,timedelta
from .forms import ProductForm,ProductImageForm


def all_orders_by_client(request, pk_client):
	client = get_object_or_404(Client, pk=pk_client)
	orders = Order.objects.filter(customer=pk_client).all()
	context = {
		"client": client,
	}
	if orders:
		context["orders"] = []
		for ord in orders:
			context["orders"].append(
				{
					"order": ord,
					"prod": [i for i in ord.products.all()],
				}
			)
	
	return render(request, "practice_2/client_orders.html", context=context)


def products_by_period(request, pk_client, period):
	if period == "week":
		t = 8
	elif period == "month":
		t = 31
	elif period == "year":
		t = 366
	else:
		t = 0
	date_period = (datetime.now() - timedelta(days=t)).strftime("%Y-%m-%d")
	print(date_period)
	client = get_object_or_404(Client, pk=pk_client)
	if t == 0:
		orders = Order.objects.filter(customer=client).order_by('-order_date')
	else:
		orders = Order.objects.filter(customer=client).filter(order_date__gt=date_period).order_by('-order_date')
	if orders:
		products_total = set()
		for order in orders:
			products_total.update([*order.products.all()])
		context = {
			"client": client,
			"products": products_total,
			"period": t-1,
		}
	else:
		context = {
			'client': client,
		}
	return render(request, 'practice_2/products_by_period.html', context=context)


def update_product_data(request, product_pk):
	product = get_object_or_404(Product, pk=product_pk)
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			product.name = form.cleaned_data['name']
			product.description = form.cleaned_data['description']
			product.price = form.cleaned_data['price']
			product.count = form.cleaned_data['count']
			product.save()
	else:
		form = ProductForm()
	return render(request, "practice_2/update_product.html", {'form': form, 'title': f'Update data of product {product.pk}'})


def add_product_img(request, product_pk):
	product = get_object_or_404(Product, pk=product_pk)
	if request.method == 'POST':
		form = ProductImageForm(request.POST, request.FILES)
		if form.is_valid():
			product.image = form.cleaned_data['image']
			product.save()
	else:
		form = ProductImageForm()
	return render(request, "practice_2/add_product_img.html",
	              {'form': form, 'title': f'Add image to product'})
