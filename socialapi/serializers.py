from rest_framework import serializers
from .models import FriendRequest
from authapi.models import MyUser

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['id', 'sender', 'receiver', 'status', 'created_at', 'updated_at']
        read_only_fields = ['sender', 'status', 'created_at', 'updated_at']

class FriendRequestActionSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=FriendRequest.STATUS_CHOICES)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['name']
