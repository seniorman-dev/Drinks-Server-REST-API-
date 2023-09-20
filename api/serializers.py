#this serializer class i created is used for converting python object (our models) to json object.
#very important for creating rest api's with django


from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']