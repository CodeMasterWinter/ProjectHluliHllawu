from . import views
from django.urls import path

urlpatterns = [
    path('construction', views.construction, name="construction"),
    path('', views.home, name="landing_home"),
    path('shop/', views.Shop, name="shop"),
    path('order/<transaction_id>/', views.ViewOrder, name="order"),
    path('checkout/<transaction_id>/', views.Checkout, name="checkout"),
    path('checkout-return/', views.CheckoutReturn, name="checkout-return"),
    path('checkout-shipping/<transaction_id>/', views.CheckoutShipping, name="checkout-shipping"),
    path('paypal-cancel/', views.paypal_cancel, name="paypal-cancel"),
    path('shop/sub-category/cakes', views.ShopCakes, name="shop-cakes"),
    path('shop/sub-category/cupcakes', views.ShopCupcakes, name="shop-cupcakes"),
    path('shop/sub-category/cookies', views.ShopCookies, name="shop-cookies"),
    path('cart/', views.cart, name="cart"),
    path('search/', views.search, name="search"),
    path('contact/', views.contact, name="contact"),
    path('shop-product/<pk>/', views.ShopProduct, name="shop-product"),
    path('Catering/Events/', views.EventCatering, name="event-catering"),
    path('Catering/', views.BusinessCatering, name="business-catering"),
]
