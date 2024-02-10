from django_unicorn.components import UnicornView, QuerySetType
from django.db.models import F
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hlulihlawu.models import OrderItem, Order


class VieworderView(UnicornView):
    orderitems: QuerySetType[OrderItem] = None
    order: QuerySetType[Order] = None
    user_pk: int
    total: float = 0
    delivery_cost: float = 0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.order_id = kwargs.get('transaction_id')
        self.orderitems = OrderItem.objects.filter(user_id=self.user_pk, order_id=self.order_id)
        self.order = Order.objects.filter(user_id=self.user_pk, transaction_id=self.order_id)
        self.get_total()
        self.get_delivery()

    def add_item(self, product_pk):
        item, created = OrderItem.objects.get_or_create(user_id=self.user_pk, product_id=product_pk, order_id=self.order_id)
        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        self.orderitems = OrderItem.objects.filter(user_id=self.user_pk, order_id=self.order_id)
        self.get_total()

    def remove_item(self, product_pk):
        item = OrderItem.objects.get(user_id=self.user_pk, product_id=product_pk, order_id=self.order_id)
        if item.quantity == 1:
            pass
        else:
            item.quantity = F('quantity') - 1
            item.save()
        self.orderitems = OrderItem.objects.filter(user_id=self.user_pk, order_id=self.order_id)
        self.get_total()

    def delete_item(self, product_pk):
        item = OrderItem.objects.get(pk=product_pk, order_id=self.order_id)
        item.delete()
        neworderitems = OrderItem.objects.filter(user_id=self.user_pk, order_id=self.order_id)
        if not neworderitems:
            neworder = Order.objects.filter(user_id=self.user_pk, transaction_id=self.order_id)
            neworder.delete()
            messages.success(self.request, "Order deleted!")
            return redirect('cart')
        else:
            self.orderitems = self.orderitems.exclude(pk=product_pk, order_id=self.order_id)
            self.get_total()

    def delete_order(self):
        order = Order.objects.get(user_id=self.user_pk, transaction_id=self.order_id)
        orderitems = order.orderitems.all()
        for orderitem in orderitems:
            orderitem.delete()
        order.delete()
        messages.success(self.request, "Order deleted!")
        return redirect('cart')

    def gotocheckout(self):

        return HttpResponseRedirect(reverse('checkout-shipping', kwargs={'transaction_id': self.order_id}))

    def get_total(self):
        self.total = sum(product.total_cost for product in self.orderitems)

    def get_delivery(self):

        if self.total < 500:
            self.delivery_cost = 500
        elif self.total >= 500:
            self.delivery_cost = 0

    def get_items(self):
        return len(self.orderitems)
