from django.shortcuts import render
from .models import Food , New_order
from rest_framework import status
from .serializer import FoodsSerializer , New_orderserializer
from rest_framework.views import APIView , Response
# Create your views here.

class Foods(APIView):
    def get(self , request):
        a = Food.objects.all()
        serialize = FoodsSerializer(a , many = True)
        return Response(data= serialize , status= status.HTTP_201_CREATED)
class  Neworder(APIView):
    def post(self , request):
        a = request.data
        serialize = New_orderserializer(a)
        if serialize.is_valid():
            serialize.save()
            return Response(data = serialize , status=status.HTTP_200_OK)
        else:
            return Response(serialize.errors , status= status.HTTP_400_BAD_REQUEST)
