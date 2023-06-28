from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        model = User
        fields = '__all__'
        # i want to hide the password
        extra_kwargs = {
            "password":{'write_only': True}
        }
        
    # method for hashing password    
    def create(self, validated_data):
        # extracted the password from th serializer
        password = validated_data.pop("password", None)
        # create the user and pass validated data without the password
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        