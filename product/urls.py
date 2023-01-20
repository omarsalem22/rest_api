from django.urls import path
from . import views
urlpatterns = [
    
    path("<int:pk>",views.Product_Detail.as_view() ,name="all"),
    path('create/', views.ProdeuctCreateAPIVeiw.as_view(), name='create'),

    
    path('list/', views. Prodeuct_list_api_view.as_view(), name='listapi'),
    path('listcreate/', views.Prodeuct_list_craete_Api.as_view(), name='listcreateapi'),
  
    path('apidef/', views. product_alt_veiw, name='apidefun'),
    path("destroy/<int:pk>",views.Product_Delete.as_view() ,name="Delete"),
    path("update/<int:pk>",views.Product_Update.as_view() ,name="Update"),

    path('listmixin/', views. ProductMixinView.as_view(), name='listapimixin'),
    



   
]