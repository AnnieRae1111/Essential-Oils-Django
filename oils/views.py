from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import EssentialOilsSerializer
from .models import EssentialOils

# Create your views here.
class OilsList(generics.ListCreateAPIView):
    queryset =EssentialOils.objects.all()
    serializer_class = EssentialOilsSerializer

class OilsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=EssentialOils.objects.all()
    serializer_class = EssentialOilsSerializer



# two views . One for getting all of the oils 
# one for getting one oil 