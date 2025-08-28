from django.contrib import admin

# Register your models here.
from .models import Menu,Order
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display= ('id','name','price','available')
    search_fields = ('name',)
    list_filter('available',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =('id','customer_name','menu_item','quantity','status','created_at')
    search_fields = ('customer_name','menu_item_name')
    list_filter = ('status','created_at')