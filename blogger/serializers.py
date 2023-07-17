from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password




class UserSerializer(serializers.ModelSerializer):
   
    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = make_password(password)
        user = User.objects.create(password=hashed_password, **validated_data)
        return user
    
            
    class Meta:
        model = User
        fields = '__all__'
        # i want to hide the password
        extra_kwargs = {
            "password":{'write_only': True}
        }
        
    

    

        