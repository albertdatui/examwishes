from rest_framework import serializers
from django.contrib.auth.models import User
#from v1.models import *
from api.models import *

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('id', 'message', 'photo', 'status', 'sender', 'receiver')

class ShopSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shop
		fields = ('name', 'identifier', 'description', 'status', 'admin')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields('id', 'name', 'description', 'videoURL', 'quantity', 'price', 'isPhotoRequired', 'shop')

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields('id', 'name', 'image', 'product')