from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from apps.main.models import Order
from datetime import datetime
from django.utils import timezone

def index(request):
	context ={
		'products': [
			{'id': 1, 'item_name': 'Dojo Shirt', 'price': 19.99, 'qty': qtyGenerator(5)},
			{'id': 2,'item_name': 'Dojo Cup', 'price': 12.99, 'qty': qtyGenerator(5)},
		],
	}
	if 'cart' not in request.session:
		request.session['num_item'] = 0

	# del request.session['cart']
	# del request.session['total']
	# del request.session['num_item']
	return render(request, 'main/index.html', context)

def cart(request):
	return render(request, 'main/cart.html')

def process_form(request):
	if 'cart' not in request.session:
		request.session['cart'] =list()
		order_list = list()
		request.session['total'] = 0

	order = {'id':len(request.session['cart']),'item':request.POST['item_name'],'price':request.POST['price'], 'quantity':request.POST['quantity'],'created_at':timezone.now().isoformat(),}
	
	order_list = request.session['cart']
	order_list.append(order)
	request.session['cart'] = order_list

	cartMath(request)

	return HttpResponseRedirect('/')

def destroy(request, order_id):
	index = 0;

	for cart in request.session['cart']:
		if cart['id'] == int(order_id):
			break
		index+=1

	first = request.session['cart'][:index]
	second = request.session['cart'][index+1:]
	request.session['cart'] = first + second
	cartMath(request)

	return HttpResponseRedirect('/cart/')

def qtyGenerator(num):
	qty = list()
	for count in range(1,num):
		qty.append(count)
	return qty

def cartMath(request):
	total = 0
	num_item = 0

	for cart in request.session['cart']:
		num_item += int(cart['quantity'])
		total += int(cart['quantity'])*float(cart['price'])
	request.session['total'] = total
	request.session['num_item'] = num_item









