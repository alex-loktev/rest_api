from rest_framework import generics
from .serializers import *
from .models import Car
from .permissions import Is0wner0rRead0nly

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarSerializer

class CarListView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = (Is0wner0rRead0nly,)