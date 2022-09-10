from django.urls import path, include, re_path

from blog.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'postlist', PostViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken'))
]

