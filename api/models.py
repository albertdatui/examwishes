from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, related_name="client")
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

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
    #boleh ditambah order date
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

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, max_length=255)
    #??image = models.ImageField(height_field=None, width_field=None, max_length=255) #Alternative: FilePathField or URLField?
    videoURL = models.URLField(blank=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    isPhotoRequired = models.BooleanField(default=False)
    shop = models.ForeignKey(Shop, related_name="product")

    def __unicode__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField(height_field=900, width_field=900, max_length=255) #Alternative: FilePathField or URLField?
    product = models.ForeignKey(Product, related_name="productImage")

    def __unicode__(self):
        return self.name
