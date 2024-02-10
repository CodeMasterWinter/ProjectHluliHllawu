from django_unicorn.components import UnicornView
from django.db.models import F
from hlulihlawu.models import CartItem
from django.shortcuts import redirect
from django.contrib import messages


class SearchView(UnicornView):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')

    def add_item(self, product_pk):
        item, created = CartItem.objects.get_or_create(user_id=self.user_pk, product_id=product_pk)
        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        messages.success(self.request, f"Added {item.product.name} to cart!")

        return redirect('cart')
