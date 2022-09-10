from blog.serializers import PostSerializer, ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
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