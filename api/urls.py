from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from api.views import *

router = DefaultRouter(trailing_slash=False)

# TODO: put urls

urlpatterns = router.urls
