from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from product.models import *
from django.forms.models import model_to_dict
import json
def api_home(request,*args,**kwargs):
    model_data=Product.objects.all().order_by("-title").first()
    data={}
    if model_data:
     data=model_to_dict(model_data,fields=['id','title','price'])
    
     
    return JsonResponse(data)

# Create your views here.

