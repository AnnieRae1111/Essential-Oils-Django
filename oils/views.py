from django.shortcuts import render

from rest_framework import generics
from .serializers import EssentialOilsSerializer

from .models import EssentialOils

# Create your views here.
class OilsList(generics.ListCreateAPIView):
    queryset =EssentialOils.objects.all()
    serializer_class = EssentialOilsSerializer

class OilsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=EssentialOils.objects.all()
    serializer_class = EssentialOilsSerializer