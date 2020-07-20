from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'confirm_password',
            'first_name',
            'last_name',
            'bio',
            'image',
            'date_joined',
        )
    
    def validate_password(self, value):
        try:
            validate_password(password=value)
            return value
        except serializers.ValidationError as e:
            raise e
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("password and confirm_password doensn't match")
        return super().validate(data)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'image',
            'date_joined',
        )


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, style={'input_type': 'password'}, max_length=50)
    
    def __init__(self, *args, **kwargs):
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.user = None
        self.fields[User.USERNAME_FIELD] = serializers.CharField(required=True, max_length=50)

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get(User.USERNAME_FIELD), password=attrs.get('password'))
        if self.user:
            return attrs
        else:
            raise serializers.ValidationError(_("Email or password is invalid"))

        

    