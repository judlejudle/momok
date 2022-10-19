from rest_framework.serializers import ModelSerializer
from .models import Restaurant


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantDetailSerializer(ModelSerializer):
    # owner = TinyUserSerializer(read_only=True)
    # amenities = AmenitySerializer(read_only=True, many=True)
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = "__all__"
        # depth = 1
