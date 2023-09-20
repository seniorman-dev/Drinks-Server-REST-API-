#this python file here is what we would use to create endpoints
#very important for creating rest api's with django

from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework import response

# Create your views here.

#"GET" REQUEST (200)
def drinks_list(request):
    #get all the drinks from database (sqlite3 😎)
    drinks = Drink.objects.all()
    #serialize them
    serializer = DrinkSerializer(instance=drinks, many = True)
    #return in json format
    return JsonResponse(data=serializer.data, safe=True)
