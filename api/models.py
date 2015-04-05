from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
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

    def __unicode__(self):
        return self.pk
