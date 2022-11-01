import imp
from django.contrib import admin
from App_main.models import *

# Register your models here.
admin.site.register(RestaurantModel)
admin.site.register(RestaurantMenuModel)
admin.site.register(RestaurantImagesModel)
admin.site.register(RestaurantRatingModel)
admin.site.register(MenuItemsModel)
admin.site.register(CartModel)
admin.site.register(Order)
