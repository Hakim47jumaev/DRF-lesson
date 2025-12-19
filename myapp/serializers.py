from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['fullname','birth_year']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'

 


class BookSerilizer(serializers.ModelSerializer):
    author=AuthorSerializer(read_only=True)

    author_id=serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )

    class Meta:
        model=Book
        fields=['title','author','author_id','price']
  



    def validate_title(self,value):
        if not value[0].isupper():
            raise serializers.ValidationError('title must start with upper latter')
        return value
    
    def validate_price(self,value):
        if  value<100:
            raise serializers.ValidationError('this price too cheap')
        return value
    
    def to_representation(self, instance):
        rep=super().to_representation(instance)
         
         
        if instance.price>1000:
            n=instance.price
            rep['rate_10%']=n-(0.1*n)
        else:
            rep['rate_10%']='not yet'


        return rep


from django.utils import timezone

class CourseSerializer(serializers.ModelSerializer):
    is_active=serializers.SerializerMethodField()

    class Meta:
        model=Course
        fields=['name','description','stack','created_at','is_active','start_at']
        read_only_fields=['created_at','is_active']


    def get_is_active(self,obj):
        return obj.start_at<timezone.now()


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"




