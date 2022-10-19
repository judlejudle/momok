from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import UsersDetailSerializer


class Users(APIView):
    def get(self, request):
        all_users = User.objects.all()
        serializer = UsersSerializer(all_users, many=True)
        return Response(serializer.data)


class UsersDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UsersDetailSerializer(user)
        return Response(serializer.data)
