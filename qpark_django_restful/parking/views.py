from django.shortcuts import render
from parking.models import UserProfile, ParkingSpot, CarInfo
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from parking.serializers import  UserProfileSerializer, UserSerializer,\
    ParkingSpotSerializer, CarInfoSerializer, UserCreateSerializer

from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

#User Views
class UserList(generics.ListAPIView):
    #renderer_classes = (JSONRenderer,TemplateHTMLRenderer )
    #template_name = "parking/base_2.html"
    queryset = User.objects.all()
    serializer_class = UserSerializer
'''
    def get(self,request,format=None):
        if request.accepted_renderer.format == 'html':
            user = User.objects.get(pk=2)
            return Response({'username': user.username}, template_name='parking/result.html')
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        data = serializer.data
        return Response(data)
   '''     
        


class UserCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    
class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
#parking slot views
class ParkingSpotList(generics.ListCreateAPIView):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

class ParkingSpotSearch(generics.ListAPIView):
    serializer_class = ParkingSpotSerializer

    def get_queryset(self):
        queryset = ParkingSpot.objects.all()
        
        search_area = self.request.query_params.get('search_area',None)
        if search_area is None:
            search_area = 10.0
        else:
            search_area = float(search_area)
        
        lon = self.request.query_params.get('lon',None)
        lat = self.request.query_params.get('lat',None)
    
        if (lon is None) | (lat is None):
            return []
        
        lon = float(lon)
        lat = float(lat)
        
        queryset = queryset.filter(lon__lte = (lon + search_area))
        queryset = queryset.filter(lon__gte = (lon - search_area))

        queryset = queryset.filter(lat__lte = (lat + search_area))
        queryset = queryset.filter(lat__gte = (lat - search_area))
        
        return queryset


#car info views
class CarInfoList(generics.ListCreateAPIView):
    queryset = CarInfo.objects.all()
    serializer_class = CarInfoSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
