from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class Register(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        role=request.data.get('role')

        if User.objects.filter(username=username).exists():
            return Response({"error":"this user already exists"},status=status.HTTP_400_BAD_REQUEST)
        
        User.objects.create_user(username=username,password=password,role=role)
        return Response({"message":"registered"},status=status.HTTP_201_CREATED)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # requires SimpleJWT blacklist enabled
            return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
 


