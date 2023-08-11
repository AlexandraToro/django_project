from django.shortcuts import render, get_object_or_404
from practice_2.models import Client, Order, Product
from datetime import datetime,timedelta


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
