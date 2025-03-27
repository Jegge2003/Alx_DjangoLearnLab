from rest_framework import generics, status 
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer

CustomUser = get_user_model()


# Register View
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user": ProfileSerializer(user).data,
            "token": token.key
        })


# Login View
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user": ProfileSerializer(user).data,
            "token": token.key
        })


# Profile View (Only accessible by the logged-in user)
class ProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Here

    def get_object(self):
        return self.request.user


# Follow another user
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # ✅ Here
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    if request.user == target_user:
        return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.add(target_user)
    return Response({"detail": f"You are now following {target_user.username}."})


# Unfollow a user
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # ✅ Here
def unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(target_user)
    return Response({"detail": f"You have unfollowed {target_user.username}."})
