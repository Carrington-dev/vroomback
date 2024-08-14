import json
from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from security.models import User
from security.mq import RabbitMQ
from security.seriliazers import UserSerializer
from vroomweb import settings

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, pk=None):
        if pk:
            serializer = UserSerializer(User.objects.get(pk))
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        user_list =  User.objects.all()
        serializer =  UserSerializer(many=True, data=user_list)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        value = super().create(request, *args, **kwargs)
        user = get_object_or_404(User, email=request.data['email'])
        password = request.data['password']
        serializer = UserSerializer(user)
        # print("Passed", password)



        try:
            publisher = RabbitMQ(**settings.RABBITMQ['default'])
            
            first_name = serializer.data['first_name']
            last_name = serializer.data['last_name']
            username = serializer.data['username']
            email = serializer.data['email']
            publisher.send_message(
                    exchange = "",  
                    routing_key = 'letterhead',
                    # routing_key = 'user.deleted.1.2.3',
                    data = json.dumps({
                        # "id": str(user.pk),
                        "username": username,
                        "email": email,
                        "first_name": first_name,
                        "last_name": last_name,
                        'password': password,
                    })
                )
        except Exception as e:
            print(e)
        
        
        return value
