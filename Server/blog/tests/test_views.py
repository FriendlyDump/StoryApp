from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from blog.views import PostViewSet


class PostViewSetViewTestCase(APITestCase):
    def setUp(self):
        User.objects.create(username='Vlad', password='T5g32asg')
        self.user = User.objects.get()
