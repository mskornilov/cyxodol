from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from common.decorators import ajax_required
from .cart import Cart
from .forms import OrderForm, Delivery_methodForm
from .models import Order
from store.models import Category, Product
# Create your views here.

@login_required
def cart_details(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        products = [p.name for p in cart]
        if form.is_valid():
            cd = form.cleaned_data
            order = Order.objects.create(cart=products, delivery_method=cd['delivery_method'],
                        name=cd['name'], email=cd['email'],
                        phone_number=cd['phone_number'],
                        address=cd['address'], post_index=cd['post_index'],
                        region=cd['region'],
                        private_info_agreement=cd['private_info_agreement'],
                        comment=cd['comment'])
            order.save()
            cart.clear()
            return redirect('cart:cart_details')
    delivery_form = Delivery_methodForm()
    form = OrderForm()
    total_price = sum(p.price for p in cart)
    return render(request, 'cart/cart_details.html', {'cart': cart,
                                                    'total_price': total_price,
                                                    'form': form,
                                                    'delivery_form': delivery_form})

@ajax_required
@login_required
def add_to_cart(request):
    cart = Cart(request)
    user = request.user
    product_id = request.POST.get('id')
    print(cart,user,product_id)
    try:
        product = get_object_or_404(Product, id=product_id)
        cart.add(product)
        print('ok')
        return JsonResponse({'status':'ok'})
    except:
        print('already_in_cart')
        return JsonResponse({'status':'ko'})
    print('ko')
    return JsonResponse({'status':'ko'})


@login_required
def remove_from_cart(request, product_id):
    if request.method == 'POST':
        cart = Cart(request)
        cart.remove(product_id)
        cart.save()
    return redirect('cart:cart_details')
