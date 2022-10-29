from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import *
from .models import *
# Create your views here.

def home(request):
	searchValue = request.GET.get('searchTerm')
	if searchValue:
		data = Shoes.objects.filter(name__icontains=searchValue)
		context = {'searchValue':searchValue, 'data': data}
	else:
		data = Shoes.objects.all()
		context = {'searchValue':searchValue, 'data': data}

	return render(request, 'home.html',context	)

@login_required
def item_details(request, shoe_id):
	data = Shoes.objects.get(pk=shoe_id)
	sizes = ShoesSize.objects.filter(shoes__id = shoe_id).order_by('-size')
	colors = ShoesColor.objects.filter(shoes__id = shoe_id)
	
	form = PurchaseForm(request.POST)
	if request.method == "POST" and form.is_valid():
		newPurchase = form.save(commit=False)
		newPurchase.user = request.user
		newPurchase.shoe_selected = data
		newPurchase.total_amount = float(float(data.price) * int(newPurchase.purchased_quantity))
		if int(data.quantity) < int(newPurchase.purchased_quantity):
			messages.error(request, 'Quantity Purchased Exceeded the Quantity remaining of the Product. Please Try Again')
			return redirect('home')
		else:
			newPurchase.save()
			updateShoeQuantity(shoe_id, newPurchase.purchased_quantity)
			messages.success(request, 'Purchased Successfully. You can now view your Purchases in MyCart ')
			return redirect('home')
	
	context = {'data': data, 'Shoecolors':colors, 'Shoesizes': sizes, 'form': form}
	return render(request, 'item_details.html', context)

def updateShoeQuantity(shoe_id, purchased_quantity):
	data = Shoes.objects.get(pk=shoe_id)
	data.quantity = int(data.quantity) - int(purchased_quantity)
	data.save()


@login_required
def myCart(request):
	cartData = ShoeCart.objects.filter(user = request.user)
	context = {'cartData':cartData}
	return render(request, 'myCart.html', context)



