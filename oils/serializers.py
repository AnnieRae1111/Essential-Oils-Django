from rest_framework import serializers
from .models import EssentialOils

class EssentialOilsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EssentialOils
        fields= ('id', 'name', 'benefits', 'aromatic_description', 'photo_url',)