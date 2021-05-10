import socketio
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from loguru import logger

from .models import User
from .serializers import UserCreateUpdateSerializer, UserSerializer


sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')


class BaseUserCreateView(APIView):
    """
    Base class for user create view.
    Also used as Register view.
    """
    def post(self, request):
        """Create user."""
        serializer = UserCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListCreateView(BaseUserCreateView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Get all user from db."""
        users = User.objects.values('id', 'first_name', 'last_name', 'phone', 'email')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, user_id):
        """Get single user from db."""
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, user_id):
        """Get user by id."""
        serializer = UserSerializer(instance=self.get_object(user_id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        """Update user by id."""
        serializer = UserCreateUpdateSerializer(
            instance=self.get_object(user_id),
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
