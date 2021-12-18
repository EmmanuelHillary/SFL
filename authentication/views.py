from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework import status


class UserRegistrationAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

# class LoginAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data['username']
#         password = request.data['password']
#         qs = User.objects.filter(username__iexact=username)
#         if qs.exists():
#             user_obj = qs.first()
#             if user_obj.check_password(password):
#                 user = authenticate(username=username, password=password)
#                 login(request, user)
#                 return Response({"success": "Login Successful"}, status=status.HTTP_201_CREATED)
#             return Response({"error": "Invalid Password"}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response({"error": "Invalid Username"}, status=status.HTTP_401_UNAUTHORIZED)
        
        
