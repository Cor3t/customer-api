from .models import Customer
from rest_framework import viewset
from .serializers import CustomerSerializer

class CustomerViewSet(viewset):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
