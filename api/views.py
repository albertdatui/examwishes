from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.models import *
from api.serializers import *

# Create your views here.
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    model = User
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        if self.request.user.is_superuser or settings.DEBUG:
            return User.objects.all()
        else:
            return User.objects.filter(id = self.request.user.id)
