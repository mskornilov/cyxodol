from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Category, Product
# Create your views here.

@login_required
def products(request, category_id=None):
    cart = Cart(request)
    cat = Category.objects.all()
    if category_id:
        products = Product.objects.filter(category=category_id)
        selected_cat = Category.objects.get(id=category_id)
        return render(request, 'store/products.html', {'category': cat,
                                                        'products': products,
                                                        'selected_cat': selected_cat,
                                                        'cart': cart})
    else:
        products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products,
                                                    'category': cat,
                                                    'cart': cart})


@login_required
def product_details(request, category_id, product_id):
    cart = Cart(request)
    category = get_object_or_404(Category, id=category_id)
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_details.html', {'cart': cart,
                                                        'category': category,
                                                        'product': product})
