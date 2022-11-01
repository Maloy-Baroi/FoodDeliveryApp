import json
from django.shortcuts import render
from App_main.models import *
from App_main.serializers import CartModelSerializer, MenuItemsModelSerializers, RestaurantModelSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
# Restaurant List


class RestaurantList(ListAPIView):
    permission_class = [AllowAny, ]
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantModelSerializer

@api_view(['GET', 'POST'])
def specific_restaurant(request, restaurant_id):
    rest = RestaurantModel.objects.get(id=restaurant_id)
    restaurant_ = {"id": rest.id, 'name': rest.restaurant_name, "address": f"{rest.restaurant_address} {rest.restaurant_area}", "city": {rest.restaurant_city}, "opening": rest.restaurant_open_time, "closing": rest.restaurant_closing_time}
    print(restaurant_)
    return Response(restaurant_)



# Food of specific restrurant
@api_view(['GET', 'POST'])
def all_item_in_menu(request, restu_id):
    restaurant = RestaurantModel.objects.get(id=restu_id)
    menu = MenuItemsModel.objects.filter(restaurant=restaurant)
    print(menu)
    menuItems = {}
    menuList = []
    for i in menu:
        # menuItems['id'] = i.id
        # menuItems['Restaurant_name'] = restaurant.restaurant_name
        # menuItems['food_name'] = i.food_name
        # menuItems['food_image'] = "http://localhost:8000/" + i.food_image.url
        # menuItems['food_description'] = i.food_description
        # menuItems['food_pricee'] = i.food_price
        # menuItems['veg'] = i.veg
        # menuItems['vegan'] = i.vegan
        menuList.append({
            'id': i.id,
            'restaurant_id': restu_id,
            'Restaurant_name': restaurant.restaurant_name,
            'food_name': i.food_name,
            'food_image': "http://localhost:8000/" + i.food_image.url,
            'food_description': i.food_description,
            'food_price': i.food_price,
            'veg': i.veg,
            'vegan': i.vegan,
        })
    return Response(menuList)


# Specific city restaurant
class CityRestaurantList(ListAPIView):
    permission_class = [AllowAny]
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantModelSerializer

    def get(self, request, restaurant_city, restaurant_area):
        # queryset = RestaurantModel.objects.all()
        queryset = RestaurantModel.objects.filter(
            Q(restaurant_city=restaurant_city), Q(restaurant_area__icontains=restaurant_area))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Specific restuarant service type
class TypeSearchRestaurantList(ListAPIView):
    permission_class = [AllowAny]
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantModelSerializer

    def get(self, request, restaurant_type):
        # queryset = RestaurantModel.objects.all()
        rest_type = str(restaurant_type).replace("-", " ")
        queryset = RestaurantModel.objects.filter(
            restuarant_service_type=rest_type)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Search Food Item in Different Restaurant
class FoodItemSearchView(ListAPIView):
    permission_class = [AllowAny]
    queryset = MenuItemsModel.objects.all()
    serializer_class = MenuItemsModelSerializers

    def get(self, request, item_name, *args, **kwargs):
        queryset = MenuItemsModel.objects.filter(
            Q(food_name__icontains=item_name))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Add to Cart
@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated, ))
def add_to_cart(request):
    pk = request.data['food_menu_id']
    restaurant_id = int(request.data['restaurant_id'])
    print(f"ID: {restaurant_id}, type: {type(restaurant_id)}")
    quantity = int(request.data['quantity'])
    restaurant = RestaurantModel.objects.get(id=restaurant_id)
    food = MenuItemsModel.objects.get(id=pk)
    try:
        cart_item = CartModel.objects.get(
            user=request.user, item=food, purchased=False)
        if cart_item.restaurant.id != restaurant.id:
            print("under If")
            prev = cart_item.restaurant
            total_cart = CartModel.objects.get(user=request.user)
            total_cart.delete()
            cart_new = CartModel.objects.create(
                user=request.user, restaurant=restaurant,  item=food, quantity=quantity, purchased=False)
            cart_new.save()
            return Response({"Success": f"Previous one was from {prev}, removed. Newly added the food from {restaurant}!!!"})
        cart_item.quantity += quantity
        cart_item.save()
        return Response({"Success": "Cart updated successfully!!!"})
    except:
        print("exception")
        total_cart = CartModel.objects.filter(user=request.user)
        if total_cart.exists() and total_cart[0].restaurant.id != restaurant_id:
            total_cart.delete()
        cart_item = CartModel.objects.create(
            user=request.user, restaurant=restaurant,  item=food, quantity=quantity, purchased=False)
        cart_item.save()
        return Response({"Success": "Food added to cart successfully!!!"})


class CartView(ListAPIView):
    permission_class = [IsAuthenticated]
    queryset = CartModel.objects.all()
    serializer_class = CartModelSerializer

    def get(self, request):
        queryset = CartModel.objects.filter(user=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
