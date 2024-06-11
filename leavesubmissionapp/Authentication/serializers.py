from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core import exceptions

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model  = User
        fields = ['email', 'user_name', 'password', 'confirm_password', 'role']

    def validate(self, data):
        password     = data.get('password')
        re_password  = data.get('confirm_password')
        if password != re_password:
            raise serializers.ValidationError("Passwords do not match.")
        
        return data
        
    def create(self,validated_data):
        role = validated_data.get('role', '').lower()
        if role == 'manager':
            user = User.objects.create_superuser(
                email      = validated_data['email'],
                user_name  = validated_data['user_name'],
                password   = validated_data['password'],
                role       = validated_data['role']
            )

            return user
        else:
            user = User.objects.create_user(
                email      = validated_data['email'],
                user_name  = validated_data['user_name'],
                password   = validated_data['password'],
                role       = validated_data['role']
            )

            return user






