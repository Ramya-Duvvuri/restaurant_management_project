from django.urls import path
from .views import *

urlpatterns = [
    path('reservations/',views.reservations_view , name ='reservations'),
    path('contact/',contact_view,name ="contact"),
    path('thank_you/',lambda request:render(request,"thankyou.html"),name ="thankyou")
    path('categories/',MenuCategoryListView.as_view(),name = 'menu-categories')
    path('api/tables/',TableListView.as_view(),name = 'table-list')
    path('api/tables/<int:pk>',TableListView.as_view(),name = 'table-detail')
]