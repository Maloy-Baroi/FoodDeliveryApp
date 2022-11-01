from django.urls import path
from App_main.views import *

app_name = 'App_main'

urlpatterns = [
    path('restaurants/', RestaurantList.as_view()),
    path('specific-restaurants/<int:restaurant_id>/', specific_restaurant),
    path('city-restaurants/<str:restaurant_city>/<str:restaurant_area>/', CityRestaurantList.as_view()),
    path('item-restaurants/<str:item_name>/', FoodItemSearchView.as_view()),
    path('service-type-restaurants/<str:restaurant_type>/', TypeSearchRestaurantList.as_view()),
    path('all-item-in-menu/<int:restu_id>/', all_item_in_menu),
    path('add-to-cart/', add_to_cart),
    path('cart-view/', CartView.as_view()),
]
