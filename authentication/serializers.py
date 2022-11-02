from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # password = serializers.CharField(
    #     read_only=True, required=True, validators=[validate_password]
    #
    # )
    # password2 = serializers.CharField(
    #     read_only=True, required=True, validators=[validate_password]
    # )

    class Meta:
        model = User
        fields = (
            'username', 'password', 'password2', 'email',
            'first_name', 'last_name'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,  # does not expose field in GET
                'min_length': 8,  # minimum length of password
                'style': {'input_type': 'password'},  # for browsable API
            },
            'password2': {
                'write_only': True,  # does not expose field in GET
                'min_length': 8,  # minimum length of password
                'style': {'input_type': 'password'},  # for browsable API
            },
        }

    def validate(self, attrs):
        if attrs['password'] == attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        user = User.objects.create(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user
