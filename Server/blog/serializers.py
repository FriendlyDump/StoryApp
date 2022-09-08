from rest_framework.serializers import ModelSerializer, ReadOnlyField
from django.contrib.auth.models import User
from blog.models import Post


class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['pk', 'title', 'content', 'author', 'status']