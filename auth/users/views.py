from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import *
from api.models import *
from .serializers import UserSerializer
import jwt
import datetime
from django.conf import settings
from functools import wraps
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

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

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return Response({
            'message': 'Successfully authenticated!',
            'jwt': token,
        })

class ValidateTokenView(APIView):
    def post(self, request):
        token = request.headers.get('Authorization')
        if token:
            try:
                token = token.split(' ')[1]  # Remove 'Bearer ' from the token
                token_obj = Token.objects.get(key=token)
                user = token_obj.user
                if user.is_active:
                    return Response({'valid': True})
                else:
                    return Response({'valid': False})
            except Token.DoesNotExist:
                return Response({'valid': False})
        else:
            return Response({'valid': False})

class UserView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            raise AuthenticationFailed('Unauthenticated')

        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except (jwt.ExpiredSignatureError, IndexError):
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        serializer = UserSerializer(user)
        return Response(serializer.data)
        
        '''
def token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return JsonResponse({'error': 'Unauthenticated'}, status=401)

        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, IndexError):
            return JsonResponse({'error': 'Unauthenticated'}, status=401)`
        
        request.user_id = payload['id']
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view

@token_required
'''
@login_required(login_url="/signin")
def home(request):
    print(request.user)
    return render(request, 'home.html')

def signup(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def employees(request):

    employees = Employee.objects.all()

    context = {
        'employees': employees,
    }

    return render(request, 'users/employees.html', context)

def inventory(request):
    return render(request, 'users/inventory.html')

def projects(request):
    return render(request, 'users/projects.html')