from rest_framework import serializers

from .models import User
from .validators import only_letters_validator, phone_number_validator


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    """User create serializer class with validators."""

    def create(self, validated_data):
        """Create new user with given fields."""
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update user with given fields and optional password."""
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email = validated_data.get('email')
        instance.phone = validated_data.get('phone')

        if validated_data.get('password'):
            instance.set_password(validated_data['password'])
       
        instance.save()

        return instance

    def validate_first_name(self, value):
        """Validate first name."""
        if not only_letters_validator(value):
            raise serializers.ValidationError(
                "User's first name must consist only of letters."
            )
        return value

    def validate_last_name(self, value):
        """Validate last name."""
        if value is None:  # Precheck for None value
            return value

        elif not only_letters_validator(value):
            raise serializers.ValidationError(
                "User's last name must consist only of letters or be null."
            )
        return value

    def validate_phone(self, value):
        """Validate phone number."""
        if value is None:
            return value

        if not phone_number_validator(value):
            raise serializers.ValidationError(
                "User's phone must be in correct format."
            )
        return value
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'password',)


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone', 'email',)
