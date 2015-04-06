from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.models import *
from api.serializers import *
from django.conf import settings

# Create your views here.
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    model = User
    #permission_classes = [AllowAny,]

    def get_queryset(self):
        if self.request.user.is_superuser or settings.DEBUG:
            return User.objects.all()
        else:
            return User.objects.filter(id = self.request.user.id)

class ShopViewSet(ModelViewSet):
	serializer_class = ShopSerializer
	model = Shop
	#permission_classes = [AllowAny,]

	def get_queryset(self):
		if self.request.user.is_superuser or settings.DEBUG:
			return Shop.objects.all()
		else:
			return Shop.objects.filter(admin = self.request.user)

class OrderViewSet(ModelViewSet):
	serializer_class = OrderSerializer
	model = Order

	def get_queryset(self):
		if self.request.user.is_superuser or settings.DEBUG:
			return Order.objects.all()
		else:
			return Order.objects.filter(sender = self.request.user)