from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from blog.models import Post, Profile

class PostTestCase(APITestCase):

    def setUp(self):
        User.objects.create(username='Vlad', password='T5g32asg')
        self.user = User.objects.get()
        Post.objects.create(
            title='first_post',
            author=self.user,
            content='T5g32 aqwfr qwfr as wr qwr qw rg'
        )
        Post.objects.create(
            title='second_post',
            author=self.user,
            content='second life post'
        )
    
    def test_post_title(self):
        first_post = Post.objects.get(title='first_post')
        second_post = Post.objects.get(title='second_post')
        self.assertEqual(first_post.title, 'first_post')
        self.assertEqual(second_post.title, 'second_post')

    def test_post_author(self):
        first_post = Post.objects.get(pk=1)
        second_post = Post.objects.get(pk=2)
        self.assertEqual(first_post.author, self.user)
        self.assertEqual(second_post.author, self.user)


class ProfileTestCase(APITestCase):

    def setUp(self):
        User.objects.create(username='Milamin', password='T5g3sw2asg')
        self.user = User.objects.get(username='Milamin')

        Profile.objects.create(
            user=self.user,
            avatar='sd/sdw/232.jpg',
            city='Lumin'
        )

    def test_profile_user(self):
        profile = Profile.objects.get(pk=1)
        self.assertEqual(profile.user, self.user)

    def test_profile_avatar(self):
        profile = Profile.objects.get(pk=1)
        self.assertEqual(profile.avatar, 'sd/sdw/232.jpg')

    def test_profile_city(self):
        profile = Profile.objects.get(pk=1)
        self.assertEqual(profile.city, 'Lumin')