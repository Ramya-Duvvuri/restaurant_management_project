from django.shortcuts import render
import requests
from .models import MenuItems
# Create your views here.
def home(request)::
    api_url  = "http://127.0.0.1:8000/api/menu/"
    response = requests.get(api_url)

    if response.status_code == 200:
        menu_items =  response.json()
    else:
        menu_items = []
    return render(request,"home.html",{"menu_items":menu_itemss0})

def menu_items(request):
    menu_items = MenuItem.objects.all()
    return render(request,"menu.html",{"menu_items":menu_items})
