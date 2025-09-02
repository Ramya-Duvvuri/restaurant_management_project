from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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
    status = models.CharField(max_digits = 10 , choices = STATUS_CHOICES,default = 'PENDING')
    created_at = models.DateTimeDield(auto_now_add = TRUE)
    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete = models.CASCADE,related_name = "items")
    menu_item = models.ForeignKey(Menu,on_delete = models.CASCADE)
    quantity = mode.PositiveIntegerField(default = 1)

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"
    def get_item_total(self):
        return self.menu_item.price * self.quantity
