from rest_framework import serializers
from .models import Category,Product
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Product
        fields = ['id','title','price','description','category','user','created_at','category_title']
        read_only_fields = ['id','user','created_at','category_title']