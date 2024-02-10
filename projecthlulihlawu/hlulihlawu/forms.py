from django import forms
from .models import Product

class ContactForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea, required=True)

class CakeForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["size", "flavour"]



class ShippingForm(forms.Form):

    provinces = [
        ("gauteng", "Gauteng"),
        ("eastern-cape", "Eastern Cape"),
        ("free-state", "Free State"),
        ("kwazulu-natal", "KwaZulu-Natal"),
        ("limpopo", "Limpopo"),
        ("mpumalanga", "Mpumalanga"),
        ("northern-cape", "Northern Cape"),
        ("north-west", "North West"),
        ("western-cape", "Western Cape")
    ]

    street = forms.CharField(required=True)
    building = forms.CharField(required=True)
    city = forms.CharField(required=True)
    province = forms.ChoiceField(required=True, choices=provinces)
    zipcode = forms.CharField(required=True)