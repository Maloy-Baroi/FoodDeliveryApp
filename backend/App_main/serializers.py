from dataclasses import field, fields
from rest_framework.serializers import ModelSerializer
from App_main.models import *


class RestaurantModelSerializer(ModelSerializer):
    class Meta:
        model = RestaurantModel
        fields = ["id",
                  "root_user",
                  "restaurant_name",
                  "restaurant_owner_name",
                  "restaurant_phone_number",
                  "restaurant_address",
                  "restaurant_area",
                  "restaurant_city",
                  "restaurant_country",
                  "restaurant_open_time",
                  "restaurant_closing_time",
                  "restaurant_type",
                  "restuarant_service_type",
                  "restaurant_registration_date",
                  "get_main_image",
                  ]
        read_only_fields = ['root_user', 'get_main_image']


class MenuItemsModelSerializers(ModelSerializer):
    class Meta:
        model = MenuItemsModel
        fields = "__all__"
        read_only_fields = ['restaurant']


class RestaurantRatingModelSerializer(ModelSerializer):
    class Meta:
        model = RestaurantRatingModel
        fields = "__all__"


class CartModelSerializer(ModelSerializer):
    class Meta:
        model = CartModel
        fields = ['get_total', 'get_user', 'get_restaurant', 'get_food_name', "purchased", "created",
                  "updated", "user", "restaurant", "item", "quantity"]
        read_only_fields = ["user",
                            "restaurant",
                            "item", 
                            "get_user",
                            "get_restaurant",
                            "get_food_name",
                            ]
