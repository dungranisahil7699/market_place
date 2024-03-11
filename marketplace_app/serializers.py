from rest_framework import serializers
from .models import Users, Product, Purchase
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )
    phone_number = serializers.CharField(
        max_length=15, 
        required=True, 
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )
    password = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'phone_number', 'password')

    def create(self, validated_data):
        user = Users.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'seller')

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('id', 'product', 'seller', 'buyer', 'purchase_price')