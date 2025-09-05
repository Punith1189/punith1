from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import redirect


def product_list(request):
    ob_products = Product.objects.all()
    return render(request, 'product_list.html', {'products': ob_products})

def product_detail(request, pk):
    ob_product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': ob_product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('view_cart')

def bill(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        item_total = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })
        total_price += item_total

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'catalog/bill.html', context)
def confirm_payment(request):
    if request.method == 'POST':
        request.session['cart'] = {}  # clear cart
        return redirect('payment_success')  # redirect after payment
    return redirect('bill')
def payment_success(request):
    return render(request, 'catalog/payment_success.html')
    from django.shortcuts import render, redirect
from .models import Product

def view_cart(request):
    cart = request.session.get('cart', {})
    products = []
    total_price = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            product.quantity = quantity
            product.subtotal = product.price * quantity
            products.append(product)
            total_price += product.subtotal
        except Product.DoesNotExist:
            continue

    context = {
        'products': products,
        'total_price': total_price,
    }
    return render(request, 'cart/view_cart.html', context)



