from django.shortcuts import render
from django.config import settings
# Create your views here.
def home_view(request):
    restaurant_name = getattr(settings,'RESTAURANT_NAME','My Restaurant')
    return render(request,'home.html',{'restaurant_name': restaurant_name})
