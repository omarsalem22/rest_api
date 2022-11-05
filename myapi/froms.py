from django import forms
from product.models import *
class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields=['title','content','price'
        
        ]
