from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_email(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        users = User.objects.filter(email__iexact=email).exclude(username__iexact=username)

        if users:
            raise ValidationError("A user with that email already exists")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class UserInfoUpdate(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserInfoUpdate, self).__init__(*args, **kwargs)

        for fieldname in ['first_name', 'last_name', 'username']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class UserEmailUpdate(forms.ModelForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserEmailUpdate, self).__init__(*args, **kwargs)

        for fieldname in ['email']:
            self.fields[fieldname].help_text = None

    def clean_email(self):

        username = self.instance.username
        get_email = self.cleaned_data["email"]
        users = User.objects.filter(email__iexact=get_email).exclude(username=username)

        if users:
            raise ValidationError("A user with that email address already exists")

        return get_email.lower()

    class Meta:
        model = User
        fields = ['email']

class UserContactUpdate(forms.ModelForm):

    phone = PhoneNumberField(region='ZA', required=False)

    def clean_phone(self):

        username = self.instance.user.id
        get_phone = self.cleaned_data["phone"]
        phone_used = Contact.objects.filter(phone__iexact=get_phone).exclude(user=username)

        if phone_used:
            raise ValidationError("A user with that phone number already exists")

        return get_phone

    class Meta:
        model = Contact
        fields = ['phone']