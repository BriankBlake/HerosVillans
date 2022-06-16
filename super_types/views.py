from .serializers import SuperTypeSerializer
from .models import Super_Type
from rest_framework import generics

class SuperTypeList(generics.ListCreateAPIView):
    queryset = Super_Type.objects.all()
    serializer_class = SuperTypeSerializer

class SuperTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Super_Type.objects.all()
    serializer_class = SuperTypeSerializer