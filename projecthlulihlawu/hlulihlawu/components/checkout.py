from django_unicorn.components import UnicornView, QuerySetType
from hlulihlawu.models import OrderItem, Order

class CheckoutView(UnicornView):
    user_products: QuerySetType[OrderItem] = None
    order: QuerySetType[Order] = None
    user_pk: int
    total: float = 0
    totalint: int
    delivery_cost: float = 0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.order_id = kwargs.get('transaction_id')
        self.user_products = OrderItem.objects.filter(order_id=self.order_id)
        self.order = Order.objects.filter(transaction_id=self.order_id).first()
        self.totalint = int(self.total)
        self.get_total()
        self.get_delivery()

    def get_cents(self):
        cents = int(self.total) * 100
        return cents

    def get_total(self):
        self.total = sum(product.total_cost for product in self.user_products)

    def get_delivery(self):

        if self.total < 500:
            self.delivery_cost = 500
        elif self.total >= 500:
            self.delivery_cost = 0

    def get_items(self):
        return len(self.user_products)
