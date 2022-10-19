from rest_framework.serializers import ModelSerializer
from .models import User


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # depth = 1


class UsersDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
