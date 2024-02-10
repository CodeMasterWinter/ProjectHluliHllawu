from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserInfoUpdate, UserEmailUpdate, UserContactUpdate
from django.contrib import messages
from django.views.generic import ListView
from hlulihlawu.models import Order, OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Let's see if you remember your login details...")
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
        'page_title': 'Sign Up',
    }

    return render(request, 'userpanel/sign_up.html', context)

@login_required
def profile(request):

    profile_headers = [{'name': 'User Info', 'stylename': 'user'},
                       {'name': 'Contact', 'stylename': 'contact'},
                       {'name': 'Track My Orders', 'stylename': 'orders'},
                       {'name': 'Purchase History', 'stylename': 'purchase'},
                       {'name': 'Cart', 'stylename': 'cart'},
                       {'name': 'Account', 'stylename': 'account'}]

    context = {
            'page_title': 'My Profile',
            'profile_headers': profile_headers,
            'empty_orders': 'You have not placed any orders yet',
        }

    return render(request, 'userpanel/user_data.html', context)

@login_required()
def infoupdate(request):

    if request.method == 'POST':
        userinfoupdate = UserInfoUpdate(request.POST, instance=request.user)

        if userinfoupdate.is_valid():
            userinfoupdate.save()
            messages.success(request, "User Info updated successfully!")
            return redirect('profile')
    else:
        userinfoupdate = UserInfoUpdate(instance=request.user)

    context = {
        'page_title': 'Update your profile',
        'userinfoform': userinfoupdate,
    }
    return render(request, 'userpanel/infoupdate.html', context)


@login_required()
def contactupdate(request):

    if request.method == 'POST':

        usercontactupdate = UserContactUpdate(request.POST, instance=request.user.contact)
        useremailupdate = UserEmailUpdate(request.POST, instance=request.user)

        if usercontactupdate.is_valid() and useremailupdate.is_valid():
            usercontactupdate.save()
            useremailupdate.save()
            messages.success(request, "Contact Details updated successfully!")
            return redirect('profile')
    else:
        usercontactupdate = UserContactUpdate(instance=request.user.contact)
        useremailupdate = UserEmailUpdate(instance=request.user)

    context = {
        'page_title': 'Update your profile',
        'usercontactform': usercontactupdate,
        'useremailform': useremailupdate,
    }

    return render(request, 'userpanel/contactupdate.html', context)

def delete_order(request, order_id):

    order = Order.objects.get(user_id=request.user.id, transaction_id=order_id)
    if order:
        orderitems = order.orderitems.all()
        for orderitem in orderitems:
            orderitem.delete()
        order.delete()
        messages.success(request, "Order deleted!")

    return redirect('profile')

"""
@login_required()
def profileupdate(request):

    if request.method == 'POST':
        profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if profileform.is_valid():
            profileform.save()
            messages.success(request, "Profile Picture updated successfully!")
            return redirect('profile')
    else:
        profileform = ProfileUpdateForm(request.POST, instance=request.user)

    context = {
        'page_title': 'Update your profile',
        'profileform': profileform,
    }
    return render(request, 'userpanel/profileupdate.html', context)
"""