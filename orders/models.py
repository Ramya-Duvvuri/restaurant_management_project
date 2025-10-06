from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from .order_status import OrderStatus
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 8;decmal_places = 2)
    def __str__(self):
        return self.name
class Order(models.Model):
    STATUS_CHOICES =[
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled')
    ]
    customer = models.ForeignKey(User,on_delete = models.CASCASE,related_name ="orders")
    total_amount = models.DecimalField(max_digits = 10,decmal_places =2)
    status = models.ForeignKey(OrderStatus,on_delete = models.SET_NULL,null = TRUE)
    created_at = models.DateTimeDield(auto_now_add = TRUE)
    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete = models.CASCADE,related_name = "items")
    menu_item = models.ForeignKey(Menu,on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 200)
    quantity = mode.PositiveIntegerField(default = 1)

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"
    def get_item_total(self):
        return self.menu_item.price * self.quantity

class RestaurantLocation(models.Model):
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 15)
    state = models.CharField(max_length = 30)
    zip_code = models.CharField(max_length = 10)

    def __str__(self):
        return f "{self.address},{self.city},{self.state},{self.zip_code}"

class OrderStatus(models.Model):
    name = models.CharField(max_length = 50,unique = TRUE)

    def __str__(self):
        return self.name

class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in =['pending','processing'])