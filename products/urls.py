from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/',MenuListView.as_view(),name ='menu-list'),
    router.register(r'menu_items',MenuListView,base_name = 'menuitem')
    urlpatterns = router.urls
    path("menu_items/",menu_items_by_category,name = "menu_items_by_category")
]