from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect

from users.forms import UserRegistrationForm
from users.views import register
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from users.models import SiteUser, UsersOrders


def order_create(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'],
                    )
                order.save()
                neworder = UsersOrders.objects.create(
                    user_id=request.user.id,
                    # order_id=Order.objects.latest('id').id,
                    order_id=order.id,
                )
                neworder.save()
                #очищаем корзину
                cart.clear()
                return render(request, 'orders/order/order_created.html', {'order': order})
        else:
            form = OrderCreateForm()
        return render(request, 'orders/order/order_create.html',
                  {'cart': cart,
                    'form': form}
                  )
    else:
        return redirect('users:register')
