from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializers import DrinkSerializer




@api_view(['GET', 'POST'])
def drinks_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(data={"drinks": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def drinks_details(request, id, format=None):
    
    #check if our object exists
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(data={"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(data={"drink": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": serializer.data}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(data={"message": "Drink deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(data={"message": "Maxed out of requests"}, status=status.HTTP_408_REQUEST_TIMEOUT)
