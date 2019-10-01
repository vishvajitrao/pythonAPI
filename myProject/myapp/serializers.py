from rest_framework import serializers
from .models import Person


class MyappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'number']

