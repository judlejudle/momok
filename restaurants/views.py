from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer
from .serializers import RestaurantDetailSerializer
from rest_framework.exceptions import NotFound


class Restaurants(APIView):
    def get(self, request):
        all_restuarants = Restaurant.objects.all()
        serializer = RestaurantSerializer(all_restuarants, many=True)
        return Response(serializer.data)


class RestuarantsDetail(APIView):
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        restaurant = self.get_object(pk)
        serializer = RestaurantDetailSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, pk):
        restaurant = self.get_object(pk)
        serializer = RestaurantDetailSerializer(
            restaurant,
            request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_restaurant = serializer.save()
            return Response(RestaurantDetailSerializer(updated_restaurant).data)
        else:
            return Response(serializer.errors)
