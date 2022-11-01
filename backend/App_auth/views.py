import imp
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from App_auth.models import *
from rest_framework.response import Response

from App_auth.serializers import RegisterSerializer


# Create your views here.
class RegisterAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['POST'])
def registerAPIView(request):
    if request.method == 'POST':
        name = request.data['full_name']
        phone = request.data['phone']
        email = request.data['email']
        password = request.data['password']
        password2 = request.data['password2']
        user = CustomUser(email=email)
        if password == password2:
            user.set_password(password)
            user.save()
            profile_ = ProfileModel(user=user, full_name=name, phone_number=phone)
            profile_.save()
            return Response({"Success": "Successfully registered!!!"})
        else:
            return Response({"Error": "Password and Confirm password should be same!!!"})
