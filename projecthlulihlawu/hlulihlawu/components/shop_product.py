from django_unicorn.components import UnicornView, QuerySetType
from django.db.models import F
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hlulihlawu.models import CartItem, Order, Product

class ShopProductView(UnicornView):

    user_products: QuerySetType[CartItem] = None
    user_pk: int
    itemcount: int
    product_price: int

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.user_products = CartItem.objects.filter(user=self.user_pk)
        self.itemcount = 1
        self.get_items()

    def add_item(self, product_pk):
        item, created = CartItem.objects.get_or_create(user_id=self.user_pk, product_id=product_pk)
        if not created:
            item.quantity = F('quantity') + self.itemcount
            item.save()
            messages.success(self.request, f"Added {self.itemcount} to cart!")
            return HttpResponseRedirect(reverse('shop-product', kwargs={'pk': product_pk}))
        elif created:
            item.quantity = self.itemcount
            item.save()
            messages.success(self.request, f"Added {self.itemcount} to cart!")
            return HttpResponseRedirect(reverse('shop-product', kwargs={'pk': product_pk}))

    def remove_item(self, product_pk):
        item = CartItem.objects.get(user_id=self.user_pk, product_id=product_pk)
        if item.quantity == 1:
            pass
        else:
            item.quantity = F('quantity') - self.itemcount
            item.save()
        self.user_products = CartItem.objects.filter(user_id=self.user_pk)

    def increment(self):
        self.itemcount += 1

    def decrement(self):
        if self.itemcount != 0:
            self.itemcount -= 1

    def get_items(self):
        return self.itemcount