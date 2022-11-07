from django.shortcuts import render
from .models import *
from myapi.serializers import Productserializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.  
class Product_Detail(generics.RetrieveAPIView):
  queryset=Product.objects.all()

  serializer_class=Productserializer

Prodeuct_DetailAPI_Veiw=Product_Detail.as_view()

  
class ProdeuctCreateAPIVeiw (generics.CreateAPIView):
  queryset=Product.objects.all()
  serializer_class=Productserializer 
  def perform_create(self,serializer):
    print("Helooooooooooooo"+serializer.validated_data)
    serializer.save()
Prodeuct_CreateAPI_Veiw=ProdeuctCreateAPIVeiw.as_view()


class Prodeuct_list_api_view(generics.ListAPIView):
  queryset=Product.objects.all()
  serializer_class=Productserializer 

class Prodeuctlist_craete_Api(generics.ListCreateAPIView):
   queryset=Product.objects.all()
   serializer_class=Productserializer 


@api_view(['POST','GET'])
   
def product_alt_veiw(request,pk=None ,*args,**kwargs):
  method=request.method
  
  if method=="GET":
    if pk is not None:
      obj=get_object_or_404(Product,pk=pk)

      data=Productserializer(obj,many=False).data

    
      return Response(data)

    queryset=Product.objects.all()
    data=Productserializer(queryset,many=True).data
    return Response(data)
  

 
  
   
  elif method=="POST":
    # "Create"
    serializer=Productserializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        
        if content==None:
          content=title
        serializer.save()
     
        return Response(serializer.data)

     
    return  Response ({"invalid":"not good"},status=400)



###########
class Product_Update(generics.UpdateAPIView):
  queryset=Product.objects.all()

  serializer_class=Productserializer
  lookup_field='pk'



########
class Product_Delete(generics.DestroyAPIView):
  queryset=Product.objects.all()

  serializer_class=Productserializer

