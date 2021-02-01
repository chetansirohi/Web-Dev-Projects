from .models import Hero
from rest_framework import serializers

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Hero
        fields =('id','name', 'alias')
