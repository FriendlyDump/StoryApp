from django.urls import path, include

from blog.views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'postlist', PostViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

