from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from product.models import *
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Productserializer   
import json
@api_view(['POST'])
def api_home(request,*args,**kwargs):
    data=request.data
    # instance=Product.objects.all().order_by("-title").first()
    # data={}
    # if instance:
    #     data =Productserializer(instance).data
    
    serializer=Productserializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)

     
    return  Response ({"invalid":"not good"},status=400)

 

