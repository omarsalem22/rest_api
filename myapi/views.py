from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from product.models import *
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Productserializer   
import json
@api_view(['GET'])
def api_home(request,*args,**kwargs):
    instance=Product.objects.all().order_by("-title").first()
    data={}
    if instance:
        data =Productserializer(instance).data
    
    
     
    return  Response (data)

 

