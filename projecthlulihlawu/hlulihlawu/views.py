from .forms import ContactForm, ShippingForm
from .models import *
import json
import requests
from random import choice
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def construction(request):

    context = {
        'page_title': 'Under Construction',
    }

    return render(request, 'hlulihlawu/construction.html', context)


def home(request):

    cakes = list()
    cupcakes = list()
    cookies = list()

    products = Product.objects.all()

    for item in products:
        if item.product_key == '1126':
            if len(cakes) == 5:
                break
            elif len(cakes) < 5:
                cakes.append(item)

    for item in products:
        if item.product_key == '1267':
            if len(cupcakes) == 5:
                break
            elif len(cupcakes) < 5:
                cupcakes.append(item)

    for item in products:
        if item.product_key == '2672':
            if len(cookies) == 5:
                break
            elif len(cookies) < 5:
                cookies.append(item)

    splash_hints = [
        'Remember to use your real details when signing up! Couriers use your details as ID for deliveries!',
        'Remember to use your real address when checking out! You don\'t wanna lose your SWEET package!',
        'Fill in your recovery contact information in settings, just in-case you get locked out of your e-mail account...',
    ]

    splash_hint = choice(splash_hints)

    context = {
        'cakes': cakes,
        'cupcakes': cupcakes,
        'cookies': cookies,
        'splash_hint': splash_hint,
    }

    return render(request, 'hlulihlawu/home.html', context)

def cart(request):

    context = {
        'page_title': 'My Cart',
    }

    return render(request, 'hlulihlawu/cart.html', context)


def search(request):

    if request.method == "POST":
        searched = request.POST['searched']

        if searched == '':
            return redirect('shop')

        else:
            products = Product.objects.filter(name__contains=searched)
            context = {
                'page_title': f'"{searched}" search results',
                'searched': searched,
                'products': products,
            }

            return render(request, 'hlulihlawu/search.html', context)
    else:

        context = {
            'page_title': 'search results',
        }

        return render(request, 'hlulihlawu/search.html', context)


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = request.POST['first_name']
            sender_surname = request.POST['last_name']
            sender_email = request.POST['email']
            sender_subject = request.POST['subject']
            sender_message = request.POST['message']

            try:
                send_mail(
                    f'{sender_subject} by {sender_name} {sender_surname}',
                    sender_message,
                    sender_email,
                    ['andromedeswebsolutions@gmail.com']
                )
                messages.success(request, f"Thanks for the feedback, {sender_name}! We'll get back to you as soon as possible!")
                return redirect('contact')

            except BadHeaderError:
                return HttpResponse("Invalid header found.")
    else:
        form = ContactForm()

    context = {
        'page_title': 'Contact Us',
        'form': form,
    }

    return render(request, 'hlulihlawu/contact.html', context)


def Shop(request):

    filterer = request.GET.get('product_key')

    if request.method == "GET":
        products = Product.objects.filter(product_key=filterer)


    if not products:
        products = Product.objects.all()


    context = {
        'page_title': 'Shop',
        'products': products,
    }

    return render(request, 'hlulihlawu/shop.html', context)

def EventCatering(request):

    context = {
        'page_title': 'Event Catering',
    }

    return render(request, 'hlulihlawu/event-catering.html', context)


def BusinessCatering(request):

    context = {
        'page_title': 'Business Catering',
    }

    return render(request, 'hlulihlawu/business-catering.html', context)


def ShopCakes(request):

    filterer = request.GET.get('product_key')

    if request.method == "GET":
        products = Product.objects.filter(product_key=filterer)


    if not products:
        products = Product.objects.filter(product_key="1126")


    context = {
        'page_title': 'Shop Cakes',
        'products': products,
    }

    return render(request, 'hlulihlawu/shop.html', context)


def ViewOrder(request, transaction_id):

    part_order = Order.objects.filter(user_id=request.user.id, transaction_id=transaction_id)

    for order in part_order:
        transaction_id = order.transaction_id

    context = {
        'page_title': 'My Order',
        'part_order': order,
        'transaction_id': transaction_id,
    }

    return render(request, 'hlulihlawu/vieworder.html', context)


def ShopCupcakes(request):

    filterer = request.GET.get('product_key')

    if request.method == "GET":
        products = Product.objects.filter(product_key=filterer)


    if not products:
        products = Product.objects.filter(product_key="1267")


    context = {
        'page_title': 'Shop Cupcakes',
        'products': products,
    }

    return render(request, 'hlulihlawu/shop.html', context)


def ShopCookies(request):

    filterer = request.GET.get('product_key')

    if request.method == "GET":
        products = Product.objects.filter(product_key=filterer)


    if not products:
        products = Product.objects.filter(product_key="2672")


    context = {
        'page_title': 'Shop Cookies',
        'products': products,
    }

    return render(request, 'hlulihlawu/shop.html', context)

@csrf_exempt
def CheckoutReturn(request):

    context = {
        'page_title': 'Order placed',
    }

    return render(request, 'hlulihlawu/return-url.html', context)


def CheckoutShipping(request, transaction_id):
    order = Order.objects.get(user_id=request.user.id, transaction_id=transaction_id)

    if request.method == "POST":
        shippingform = ShippingForm(request.POST)

        if shippingform.is_valid():
            order.street = shippingform.cleaned_data["street"]
            order.building = shippingform.cleaned_data["building"]
            order.city = shippingform.cleaned_data["city"]
            order.province = shippingform.cleaned_data["province"]
            order.zipcode = shippingform.cleaned_data["zipcode"]
            order.save()

        return HttpResponseRedirect(reverse('checkout', kwargs={'transaction_id': order.transaction_id}))
    else:
        shippingform = ShippingForm()

    context = {
        'page_title': 'Shipping Details',
        'shippingform': shippingform,
        'order': order,
    }

    return render(request, 'hlulihlawu/checkout-shipping.html', context)

def paypal_cancel(request):

    context = {
        'page_title': 'Order canceled',
    }

    return render(request, 'hlulihlawu/cancel-url.html', context)

@csrf_exempt
def Checkout(request, transaction_id):

    if request.method == "POST":
        result_dict = json.loads(request.body)

        SECRET_KEY = 'sk_test_82b9f4afR4LPbPz20064466a8e14'

        response = requests.post('https://online.yoco.com/v1/charges/',
        headers={'X-Auth-Secret-Key': SECRET_KEY},
        json={
                'token': result_dict["res_id"],
                'amountInCents': result_dict["cents"],
                'currency': 'ZAR',
            }
        )

        if response.json()["status"] == 'successful' and response.status_code == 201:
            if response.json()["amountInCents"] == int(result_dict["cents"]) and response.json()["currency"] == 'ZAR':
                order = Order.objects.filter(transaction_id=transaction_id, user_id=request.user.id).first()
                order.completed = "checked-out"
                order.name += f' -- paid'
                order.save()

    context = {
        'page_title': 'Checkout',
        'transaction_id': transaction_id,
    }

    return render(request, 'hlulihlawu/checkout.html', context)


def ShopProduct(request, pk):

    products = Product.objects.filter(pk=pk)

    context = {
        'page_title': 'Shop',
        'products': products,
    }

    return render(request, 'hlulihlawu/shop-product.html', context)