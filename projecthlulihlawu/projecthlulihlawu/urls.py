from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from userpanel import views as userpanel_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hlulihlawu.urls')),
    path('sign_up/', userpanel_views.sign_up, name='sign_up'),
    path('login/', auth_views.LoginView.as_view(template_name='userpanel/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userpanel/logout.html'), name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
            template_name='userpanel/reset-password.html'),
            name='reset-password'),

    path('password_reset/', auth_views.PasswordResetDoneView.as_view(
            template_name='userpanel/password-reset.html'),
            name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='userpanel/password-reset-confirm.html'),
            name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='userpanel/password-reset-confirm.html'),
            name='password_reset_complete'),

    path('profile/', userpanel_views.profile, name='profile'),
    path('unicorn/', include('django_unicorn.urls')),
    path('update_profile_info/', userpanel_views.infoupdate, name='infoupdate'),
    path('update_contact_info/', userpanel_views.contactupdate, name='contactupdate'),
    path('delete_order/<order_id>', userpanel_views.delete_order, name='delete-order'),

]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)