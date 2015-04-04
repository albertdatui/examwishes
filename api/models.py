from django.db import models
from django.contrib.auth.models import User

#TODO: shop status

class Customer(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, related_name="customer")
    address = models.CharField(max_length=255)

    def __unicode__(self):
        return self.user.first_name


class Order(models.Model):
    PENDING = 'PE'
    DELIVERED = 'DE'
    PAID = 'PA'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
        (PAID, 'Paid'),

    )
    message = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)
    sender = models.ForeignKey(Customer, related_name="ordered")
    receiver = models.ForeignKey(Customer, related_name="received")
    #productnya ilang

    def __unicode__(self):
        return self.pk


class Shop(models.Model):
    OPEN = 'O'
    CLOSE = 'C'
    TEST = 'T'
    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (CLOSE, "Close"),
        (TEST, 'Test'),
    )
    name = models.TextField(blank=False)
    #how to ensure that the identifier is unique?
    identifier = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=CLOSE)
    admin = models.ForeignKey(Customer, related_name="shop", blank=True)

    def __unicode__(self):
        return self.name