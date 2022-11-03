from django.shortcuts import render
from .models import *

# Create your views here.
def all(request):
    pro=Product.objects.all()
    context={"pro":pro}

    return render(request,'all.html',context)