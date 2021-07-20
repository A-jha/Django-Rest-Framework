from rest_framework import serializers
from .models import Artical


class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artical
        fields = ['id', 'title', 'author', 'email']
