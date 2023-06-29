from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.ReadOnlyField(source = 'user.password')
    
    class Meta:
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
        