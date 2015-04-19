from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from api.views import *

router = DefaultRouter(trailing_slash=False)

router.register(
    r'user',
    UserViewSet,
    base_name='user'
)

router.register(
	r'shop',
	ShopViewSet,
	base_name='shop'
)

router.register(
	r'order',
	OrderViewSet,
	base_name='order'
)

router.register(
	r'group',
	GroupViewSet,
	base_name='group'
)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^permission/(?P<pk>\d+)/$', PermissionDetail.as_view(), name='permission-detail'),
    url('', include('social.apps.django_app.urls', namespace='social')),
]