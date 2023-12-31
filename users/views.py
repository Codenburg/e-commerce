from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serialzers import RegisterUserSerializer, MyTokenObtainPairSerializer

@api_view(['POST'])
def register(req):
    data = req.data
    user = User.objects.create(
        email=data['email'],
        name=data['name'],
        last_name=data['last_name'],
        password=make_password(data['password'])
    )
    serializer = RegisterUserSerializer(user,many=False)
    return Response(serializer.data)

#Return access_token and refresh_token
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

