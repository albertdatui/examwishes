from rest_framework import serializers
from django.contrib.auth.models import User
#from v1.models import *
from api.models import *

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('id', 'message', 'photo', 'status', 'sender', 'receiver', 'product')

class ShopSerializer(serializers.ModelSerializer):
	product = serializers.PrimaryKeyRelatedField(many=True, queryset=Shop.objects.all())
	manager = serializers.PrimaryKeyRelatedField(many=True, queryset=Customer.objects.all())
	admin = serializers.ReadOnlyField(source='admin.username')
	class Meta:
		model = Shop
		fields = ('name', 'identifier', 'description', 'status', 'admin', 'product', 'manager')

class ProductSerializer(serializers.ModelSerializer):
	#kalo gw gak salah inget, lu harus specify di sini buat nge-query image
	class Meta:
		model = Product
		fields('id', 'name', 'description', 'videoURL', 'quantity', 'price', 'isPhotoRequired', 'shop')

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields('id', 'name', 'image', 'product')