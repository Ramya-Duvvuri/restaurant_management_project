from django.shortcuts import render
from django.config import settings
from .serializers import MenuCategorySerializer

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


# Create your views here.
def home_view(request):
    restaurant_name = getattr(settings,'RESTAURANT_NAME','My Restaurant')
    phone_number = getattr(settings,'RESTAURANT_PHONE','Phone not available')
    render request(request,'home.html',{
        'restaurant_name':restaurant_name,
        'phone_number':phone_number
    })
def reservations_view(request):
    return render(request,'reservations.html')
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return.redirect("Thank_you")
    else:
        form = ContactForm()
    return render(request,"contact_form.html",{"form":form})


