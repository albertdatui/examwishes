from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
	address = serializers.CharField(source='client.address')
	phone = serializers.CharField(source='client.phone')

	class Meta:
		model = User
		fields = (
			'id',
			'username',
			'first_name',
			'last_name',
			'address',
			'phone',
			'email',
			'password',
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
			'message',
			'photo',
			'status',
			'sender',
			'sender_alias',
			'receiver',
			'receiver_alias',
			'product',
		)


class ShopSerializer(serializers.HyperlinkedModelSerializer):
	product = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail',read_only=True)
	manager = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

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


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'description', 'videoURL', 'quantity', 'price', 'isPhotoRequired', 'shop')


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission


class ImageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Image
		fields = ('id', 'name', 'image', 'product')