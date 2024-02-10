from django_unicorn.components import UnicornView, QuerySetType
from userpanel.views import delete_order
from hlulihlawu.models import CartItem, OrderItem, Order, User


class UserDataView(UnicornView):

    orders: QuerySetType[Order] = None
    user_pk: int

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.orders = Order.objects.filter(user_id=self.user_pk)