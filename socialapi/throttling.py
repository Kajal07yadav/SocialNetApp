from rest_framework.throttling import UserRateThrottle

class FriendRequestRateThrottle(UserRateThrottle):
    scope = 'friend_request'