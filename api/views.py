from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from templates import *
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

class GroupViewSet(ModelViewSet):
	serializer_class = GroupSerializer
	model = Group

	def get_queryset(self):
		if self.request.user.is_superuser or settings.DEBUG:
			return Group.objects.all()
		else:
			return Group.objects.filter(sender = self.request.user)

class PermissionDetail(generics.RetrieveAPIView):
	queryset = Permission.objects.all()
	serializer_class = PermissionSerializer


def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/api/login/')