from rest_framework.serializers import ModelSerializer
from security.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'last_name', 'first_name',)


