from rest_framework import serializers
from product.models import *
class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['title','content','price','sale_price','get_disc'
        
        ]
    def disc(self,obj):
            return obj.get_disc()
