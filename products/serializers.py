from rest_framework import serializers
from .models import Item
from .modes import MenuItems

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
class MenuItemsSeriaizer(serializer.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['id','name','description','price']

        def validate_price(self,value):
            if value <0 :
                raise serializers.validationError('Price must be a positive value')
                return value