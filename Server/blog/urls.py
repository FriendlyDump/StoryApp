from django.urls import re_path
from blog.views import *

urlpatterns = [
    re_path(r'^api/v1/postlist/$', PostApiView.as_view(), name='home'),
    re_path(r'^api/v1/postlist/(?P<pk>[0-9]+)$', PostApiView.as_view()),
]

