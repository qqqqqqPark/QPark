from rest_framework import serializers
from parking.models import UserProfile, ParkingSpot, CarInfo
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.Serializer):
    
    user = serializers.ReadOnlyField(source='user.username')

    evaluation = serializers.FloatField(default=0.0, required=False)
    evalNum = serializers.FloatField(default=0, required=False)

    class Meta:
        model = UserProfile
        fields = ('evaluation', 'evalNum')


class UserSerializer(serializers.ModelSerializer):

    user_profile = UserProfileSerializer()
    park_spot = serializers.PrimaryKeyRelatedField(many=True,
                                                   queryset=ParkingSpot.objects.all())
    car_info = serializers.PrimaryKeyRelatedField(many=True,
                                                  queryset=CarInfo.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username','password', 'email', 'user_profile', 'park_spot', 'car_info')



class UserCreateSerializer(serializers.ModelSerializer):
    
    user_profile = UserProfileSerializer()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email','user_profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('user_profile')
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        UserProfile.objects.create(user=user,**profile_data)
        return user


class ParkingSpotSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ParkingSpot
        fields = ('id', 'owner', 'availability', 'carPlateNo',
                  'state', 'city', 'street', 'houseNo', 'zipCode',
                  'length', 'width', 'height', 'lon', 'lat')

class CarInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CarInfo
        fields = ('id','owner', 'plateNo', 'parkId', 'color',
                  'length', 'width', 'height')
