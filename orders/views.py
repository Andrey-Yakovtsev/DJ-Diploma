from django.shortcuts import render

from users.forms import UserRegistrationForm
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from users.models import SiteUser


def order_create(request):
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
                    quantity=item['quantity']
                )
            order.save()
            # new_user = form.save(commit=False)  #Здесь создавался новый юзер при формировании заказа
            # SiteUser.objects.create(              # Пока все это заменю на лог ин при оформлении
            #     username=new_user.username,
            #     first_name=new_user.first_name,
            #     last_name=new_user.last_name,
            #     email=new_user.email,
            #     address=new_user.address,
            #     city=new_user.city,
            #     phone=new_user.phone,
            #     orders=Order.objects.latest('created')
            # )
            # new_user.save()
            #очищаем корзину
            cart.clear()
            return render(request, 'orders/order/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/order_create.html',
                  {'cart': cart,
                    'form': form}
                  )