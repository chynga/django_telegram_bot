from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
import requests

from base.models import *
from .serializers import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/register',
        '/api/messages',
        '/api/messages/send',
        '/api/token',
        '/api/token/refresh',
    ]
    
    return Response(routes)

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    
@api_view(['GET'])
def get_messages(request):
    profile = Profile.objects.get(user_id = request.user)
    messages = Message.objects.filter(profile = profile)
    serializer = MessageSerializer(messages, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def send_message(request):
    profile = Profile.objects.get(user_id = request.user)
    text = request.data['text']
    Message(
        profile = profile,
        text = text,
    ).save()

    try:
        apiURL = f'https://api.telegram.org/bot{settings.TOKEN}/sendMessage'
        json = {
            'chat_id': profile.chat_id, 
            'text': text
        }
        requests.post(apiURL, json = json)
    except Exception as e:
        print(e)
    
    return Response(status = 200)