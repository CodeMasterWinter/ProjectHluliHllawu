from django.db import models
from uuid import uuid4
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Product(models.Model):

    categories = [
        ("1126", "Cakes"),
        ("1267", "Cupcakes"),
        ("2672", "Cookies"),
        ("2762", "Platters")
    ]

    cake_parameters = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("P", "Party")
    ]

    flavor = [
        ("V", "Vanilla"),
        ("C", "Chocolate"),
        ("U", "Non-Customizable"),
    ]

    description = models.TextField(default="It's a cake", max_length=250)
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(default='default-cake.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_key = models.CharField(max_length=100, choices=categories, default='1126')
    size = models.CharField(max_length=100, choices=cake_parameters, default='M')
    flavour = models.CharField(max_length=100, choices=flavor, default='V')
    size_avail = models.BooleanField(default=True)
    flavour_avail = models.BooleanField(default=True)

    def __str__(self):

        return self.name


    def get_absolute_url(self):
        return reverse('shop-product', kwargs={'product_key': self.product_key, 'pk': self.pk})


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.CharField(default='order_id not presented', editable=False, max_length=36)
    name = models.CharField(max_length=200, default=f'{User.username}--{product.name}')

    def __str__(self):
        return self.name

    @property
    def total_cost(self):
        return self.product.price * self.quantity

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user}--{self.product.name}'

    @property
    def total_cost(self):
        return self.product.price * self.quantity


def gen_uuid():
    return str(uuid4())


class Order(models.Model):

    order_stages = [
        ("ordered", "Awaiting Checkout"),
        ("checked-out", "Order Placed"),
        ("preparing", "Being Prepared"),
        ("prepared", "Completed, awaiting delivery"),
        ("complete", "Delivered, Complete")
    ]

    provinces = [
        ("gauteng", "Gauteng"),
        ("eastern-cape", "Eastern Cape"),
        ("free-state", "Free State"),
        ("kwaZulu-natal", "KwaZulu-Natal"),
        ("limpopo", "Limpopo"),
        ("mpumalanga", "Mpumalanga"),
        ("northern-cape", "Northern Cape"),
        ("north-west", "North West"),
        ("western-cape", "Western Cape")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=f'{User.username} order')
    orderitems = models.ManyToManyField(OrderItem)
    completed = models.CharField(max_length=50, choices=order_stages, default="ordered")
    transaction_id = models.CharField(unique=True, primary_key=True, default=gen_uuid, editable=False, max_length=36)
    created = models.DateTimeField(default=timezone.now)

    street = models.CharField(max_length=200, null=True)
    building = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    province = models.CharField(max_length=200, choices=provinces, null=True, default="gauteng")
    zipcode = models.CharField(max_length=4, null=True)

    @property
    def order_total(self):
        orderitems = OrderItem.objects.filter(user_id=self.user.id, order_id=self.transaction_id)
        total = sum([item.total_cost for item in orderitems])
        return total

    def __str__(self):
        return self.name


"""
class Order(models.Model):
    orderitem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username} order'

    def __str__(self):
        return self.product.name

    @property
    def total_cost(self):
        return self.product.price * self.quantity
"""
"""

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=False, null=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingModel(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    province = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)

"""


