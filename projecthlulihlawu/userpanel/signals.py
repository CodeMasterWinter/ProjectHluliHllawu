from .models import Contact
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_contact(sender, instance, created, **kwaargs):

    if created:
        Contact.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_contact(sender, instance, **kwaargs):

    instance.contact.save()