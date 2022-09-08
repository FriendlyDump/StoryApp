from django.urls import path, re_path
from blog.views import *

urlpatterns = [
    re_path(r'^api/v1/postlist/$', PostView.as_view(), name='home'),
    re_path(r'^api/v1/postlist/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='post-detail'),
]

