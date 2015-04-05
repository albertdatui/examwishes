from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
	address = serializers.URLField(source='client.address')
	phone = serializers.URLField(source='client.phone')

	class Meta:
		model = User
		fields = (
			'id',
			'name',
			'address',
			'phone',
			'email',
			'password',
			'groups',
		)

		write_only_fields = ('password',)

	def create(self, validated_data):
        client = Client.objects.create(**validated_data.get('client'))
        # must remove the client data before creating user
        del validated_data['client']
        user = User.objects.create_user(**validated_data)
        # establish the relationship
        client.user = user
        return user


class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Order
		fields = (
			'id',
			'alias',
			'message',
			'photo',
			'status',
			'sender',
			'receiver',
			'product',
		)


class ShopSerializer(serializers.HyperlinkedModelSerializer):
	product = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail',read_only=True)
	manager = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail')

	class Meta:
		model = Shop
		fields = (
			'id',
			'name',
			'identifier',
			'description',
			'status',
			'admin',
			'product',
			'manager',
		)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields('id', 'name', 'description', 'videoURL', 'quantity', 'price', 'isPhotoRequired', 'shop')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Image
		fields('id', 'name', 'image', 'product')
