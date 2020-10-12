from django.shortcuts import render

from users.forms import UserRegistrationForm
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from users.models import User


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            order.save()
            new_user = form.save(commit=False)
            User.objects.create(
                username=new_user.username,
                first_name=new_user.first_name,
                last_name=new_user.last_name,
                email=new_user.email,
                address=new_user.address,
                city=new_user.city,
                phone=new_user.phone,
                orders=Order.objects.latest('created')
            )
            new_user.save()
            #очищаем корзину
            cart.clear()
            return render(request, 'orders/order/order_created.html', {'order': order, 'new_user': new_user})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/order_create.html',
                  {'cart': cart,
                    'form': form}
                  )