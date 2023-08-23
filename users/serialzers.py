from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'last_name', 'password']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
        Indicar que pasarle al JWT
    '''
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['avatar'] = user.avatar.url  # Solo la URL no el archivo en si
        token['is_staff'] = user.is_staff

        return token
