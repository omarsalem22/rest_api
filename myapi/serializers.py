from rest_framework import serializers
from product.models import *
class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','content','price','sale_price','get_disc'
        
        ]
    def disc(self,obj):
        if not hasattr(obj,'id'):
            return None 
        if not  isinstance(obj,Product):
                 
            return obj.get_disc()
