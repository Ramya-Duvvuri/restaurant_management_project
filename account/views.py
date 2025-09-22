from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import DatabaseError
from .models import Restaurant
def signup_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request,'Account created successfully.Please log in')
                return redirect('login')
            else:
                messages.error(request,'Please correct the errors below')
        except DatabaseError as db_error:
            messages.error(request,f"Database error has been occurred: {db_error}")
        except Exception as e:
            messages.error(request,f"An unexpected error has been occured:{e}")
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def homepage(request):
    restaurant = Restaurant.object.first()
    return render(request,'homepage.html',{'restaurant':restaurant})


# Create your views here.
