from django_unicorn.components import UnicornView
from django.db.models import F
from django.contrib import messages
from hlulihlawu.models import CartItem

class ShopView(UnicornView):
    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.user_products = CartItem.objects.filter(user=self.user_pk)

    def add_item(self, product_pk):
        item, created = CartItem.objects.get_or_create(user_id=self.user_pk, product_id=product_pk)
        if not created:
            item.quantity = F('quantity') + 1
            item.save()
            messages.success(self.request, f"Added {item.product.name} to cart!")
        self.user_products = CartItem.objects.filter(user=self.user_pk)
        self.get_total()

    def remove_item(self, product_pk):
        item = CartItem.objects.get(user_id=self.user_pk, product_id=product_pk)
        item.quantity = F('quantity') - 1
        item.save()
        self.user_products = CartItem.objects.filter(user_id=self.user_pk)
        self.get_total()

    def delete_item(self, product_pk):
        item = CartItem.objects.get(pk=product_pk)
        item.delete()
        self.user_products = self.user_products.exclude(pk=product_pk)
        self.get_total()

    def get_total(self):
        self.total = sum(product.total_cost for product in self.user_products)

    def get_items(self):
        return len(self.user_products)
