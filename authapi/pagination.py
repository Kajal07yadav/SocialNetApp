from rest_framework.pagination import CursorPagination

class UserSearchProfilePagination(CursorPagination):
    page_size = 10