from rest_framework import serializers
from .models import *

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('id','doctor', 'name', 'date', 'time', 'kind')

class PhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physicians
        fields = ('name','email')