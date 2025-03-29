from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import generics, permissions
from rest_framework import status
from .models import Post, Like
from notifications.utils import create_notification  # You’ll create this next
from accounts.models import CustomUser
from rest_framework.views import APIView
from notifications.models import Notification


# Create your views here.
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.author == request.user
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the users the current user follows
        following_users = self.request.user.following.all()
        # Return posts from followed users ordered by newest first
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if created:
        create_notification(request.user, post.author, 'liked', post)
        return Response({'message': 'Post liked!'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'You already liked this post.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = Post.objects.get(pk=pk)
    Like.objects.filter(post=post, user=request.user).delete()
    return Response({'message': 'Post unliked!'}, status=status.HTTP_200_OK)

