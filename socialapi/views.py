"""
Views for Social Networking Application APIs
"""

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authapi.models import MyUser
from .models import FriendRequest
from .serializers import FriendRequestSerializer, FriendRequestActionSerializer, UserSerializer
from django.db.models import Q
from .throttling import FriendRequestRateThrottle



class SendFRView(generics.CreateAPIView):
    """View for manage friend request send APIs"""

    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [FriendRequestRateThrottle]

    def create(self, request, *args, **kwargs):
        receiver_name = request.data.get('receiver')
        try:
            receiver = MyUser.objects.get(name=receiver_name)
        except MyUser.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if receiver == request.user:
            return Response({'detail': 'You cannot send a friend request to yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        friend_request, created = FriendRequest.objects.get_or_create(sender=request.user, receiver=receiver)
        if not created:
            return Response({'detail': 'Friend request already sent.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Friend request sent.'}, status=status.HTTP_201_CREATED)


class RespondFRView(generics.UpdateAPIView):
    """View for manage response of Accept or Reject friend request APIs"""

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestActionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        friend_request = self.get_object()

        if friend_request.receiver != request.user:
            return Response({'detail': 'Not authorized to respond to this friend request.'}, status=status.HTTP_403_FORBIDDEN)

        status_response = request.data.get('status')

        if status_response not in ['accepted', 'rejected']:
            return Response({'detail': 'Invalid status.'}, status=status.HTTP_400_BAD_REQUEST)

        friend_request.status = status_response
        friend_request.save()
        return Response({'detail': f'Friend request {status_response}.'}, status=status.HTTP_200_OK)


class YourFrAcceptedView(generics.ListAPIView):
    """View for Listing the user's name who have accepted friend request """

    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user

        accepted_users = MyUser.objects.filter(
            Q(sent_requests__receiver=user, sent_requests__status='accepted') |
            Q(received_requests__sender=user, received_requests__status='accepted')
        ).distinct()
        return accepted_users


class YourFrRejectedView(generics.ListAPIView):
    """View for Listing the user's name who have Rejected friend request """

    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user

        accepted_users = MyUser.objects.filter(
            Q(sent_requests__receiver=user, sent_requests__status='rejected') |
            Q(received_requests__sender=user, received_requests__status='rejected')
        ).distinct()
        return accepted_users


class ListAcceptsFRView(generics.ListAPIView):
    """View for listing Accepted user's request """

    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(receiver=self.request.user, status='accepted')


class ListRejectedFRView(generics.ListAPIView):
    """View for listing Rejected user's request """

    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(receiver=self.request.user, status='rejected')


class ListPendingFRView(generics.ListAPIView):
    """View for listing pending user's request """

    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(receiver=self.request.user, status='pending')
