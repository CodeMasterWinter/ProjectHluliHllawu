from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Contact(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = User.email
    phone = PhoneNumberField(region='ZA', null=True)

    def __str__(self):
        return f'{self.user.username} Contact Model'
