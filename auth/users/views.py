from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import *
from .serializers import *
import jwt, datetime

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now(datetime.timezone.utc),
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({
            'message': 'Successfully authenticated!',
            'jwt': token,
        })
    
class UserView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            raise AuthenticationFailed('Unauthenticated')

        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except (jwt.ExpiredSignatureError, IndexError):
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        serializer = UserSerializer(user)

        return Response(serializer.data)