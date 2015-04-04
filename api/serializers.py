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