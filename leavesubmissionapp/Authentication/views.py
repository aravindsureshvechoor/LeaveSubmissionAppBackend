from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from django.contrib.auth import get_user_model,authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken
from django.http import JsonResponse


User = get_user_model()



# Create your views here.
class UserRegistrationView(APIView):
    def post(self,request):
        data                 = request.data
        role                 = data.get('role')

        serialized_user_data = UserRegistrationSerializer(data=data)
        
        if not serialized_user_data.is_valid():
            return Response(serialized_user_data.errors,status=status.HTTP_400_BAD_REQUEST)
        user                 = serialized_user_data.create(serialized_user_data.validated_data)
        user.save()
        return Response({'success':'User registerd successfully','role':role},status=status.HTTP_201_CREATED)



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access' : str(refresh.access_token),
    }



class UserLoginView(APIView):
    def post(self,request):
        data     = request.data
        email    = data.get('email')
        password = data.get('password')
        user     = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response = JsonResponse({
                    "data": data,
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "name": user.user_name,
                    }
                })
                

                response.data = {"Success" : "Login successfully","data":data}
                return response
        else:
            return Response({'invalid':'invalid username or password'},status=status.HTTP_401_UNAUTHORIZED)