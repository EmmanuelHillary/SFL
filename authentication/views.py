from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class UserRegistrationAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def get_serializer_context(self):
        return {"request": self.request}

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = authenticate(username=username, password=password)
                login(request, user)
                return Response({"success": "Login Successful"}, status=status.HTTP_200_OK)
            return Response({"password": "Invalid Password"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"username": "Invalid Username"}, status=status.HTTP_401_UNAUTHORIZED)
        
        
