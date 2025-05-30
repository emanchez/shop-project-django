from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.db.models.functions import Random
from .cart import Cart

def index(request):
    featured_products = Product.objects.filter(available=True).order_by(Random())[:3]
    return render(request, 'index.html', {'featured_products': featured_products})

def shop(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')