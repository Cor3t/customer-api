from .views import CustomerViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('customer', CustomerViewSet, basename='customer')


urlpatterns = [
    path('customer', include(router))
]