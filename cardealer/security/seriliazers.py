from rest_framework import serializers
from security.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"},  write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'last_name', 'first_name', 'password',)


    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user