from rest_framework.serializers import ModelSerializer, ReadOnlyField
from django.contrib.auth.models import User
from blog.models import Post, Profile


class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username']

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"