from rest_framework import serializers
from .modes import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id','name']