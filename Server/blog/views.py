from blog.serializers import PostSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from blog.models import Post, Profile


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return Post.objects.filter(author=user)
        else: 
            return Post.objects.all()


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileApiView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, author_id):
        author = User.objects.get(pk=author_id)
        posts = Post.objects.filter(author=author)
        return Response({
            "posts": PostSerializer(posts, many=True).data
            })