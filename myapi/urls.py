
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
   
    path("",views.api_home,name="api_home"),
    path('products/', include('product.urls')),
    path('auth/',obtain_auth_token),
    


]