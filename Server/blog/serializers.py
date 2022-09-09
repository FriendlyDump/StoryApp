from rest_framework.serializers import ModelSerializer, ReadOnlyField
from django.contrib.auth.models import User
from blog.models import Post, Profile


class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super(PostSerializer, self).create(validated_data)

    class Meta:
        model = Post
        fields = "__all__"


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"