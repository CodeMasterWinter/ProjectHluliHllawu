from django_unicorn.components import UnicornView, QuerySetType
from django.contrib.auth.models import User
from django.db.models import F
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hlulihlawu.models import CartItem, OrderItem, Order, User


class CartView(UnicornView):

    out_orders: QuerySetType[Order] = None
    user_products: QuerySetType[CartItem] = None
    user_pk: int
    total: float = 0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.out_orders = Order.objects.filter(user_id=self.user_pk, completed="ordered")
        self.user_products = CartItem.objects.filter(user_id=self.user_pk)
        self.get_total()

    def add_item(self, product_pk):
        item, created = CartItem.objects.get_or_create(user_id=self.user_pk, product_id=product_pk)
        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        self.user_products = CartItem.objects.filter(user_id=self.user_pk)
        self.get_total()

    def remove_item(self, product_pk):
        item = CartItem.objects.get(user_id=self.user_pk, product_id=product_pk)
        if item.quantity == 1:
            pass
        else:
            item.quantity = F('quantity') - 1
            item.save()
        self.user_products = CartItem.objects.filter(user_id=self.user_pk)
        self.get_total()

    def delete_item(self, product_pk):
        item = CartItem.objects.get(user_id=self.user_pk, pk=product_pk)
        item.delete()
        self.user_products = self.user_products.exclude(pk=product_pk)
        self.get_total()

    def create_order(self):

        checkedorders = Order.objects.filter(user_id=self.user_pk).exclude(completed="ordered")
        if checkedorders:
            messages.error(self.request,
                           """You have already placed an order. To avoid any backlog,
                           we have limited all customers to one order at a time. However, 
                           You may still add items to your cart for your next order! You lucky duck!""")

            return redirect('cart')
        else:
            if self.user_products:
                order = Order.objects.create(user_id=self.user_pk)
                ordercount = Order.objects.filter(user_id=self.user_pk).count()
                order.name = f'{self.request.user.username} order {ordercount}'

                for item in self.user_products:
                        orderitem = OrderItem.objects.create(user_id=self.user_pk)
                        orderitem.order_id = order.transaction_id
                        orderitem.quantity = item.quantity
                        orderitem.product = item.product
                        orderitem.name = f'{order.name}--{order.transaction_id}--{item.product.name}'
                        orderitem.save()
                        order.orderitems.add(orderitem)
                        order.save()

                self.request.session['order_id'] = order.transaction_id
                messages.success(self.request, "Order created!")
                return HttpResponseRedirect(reverse('checkout-shipping', kwargs={'transaction_id': order.transaction_id}))
            else:
                messages.error(self.request, "You can't place an order with an empty cart")
                return redirect('cart')

    def get_total(self):
        self.total = sum(product.total_cost for product in self.user_products)

    def get_items(self):
        return len(self.user_products)