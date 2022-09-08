from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post
from blog.serializers import PostSerializer


class PostApiView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)    
        if request.user.is_authenticated:
            if pk:
                post = Post.objects.filter(pk=pk)
                return Response({
                "post": PostSerializer(post, many=True).data
                })
            else:
                posts = Post.objects.filter(author=request.user)
                return Response({
                    "posts": PostSerializer(posts, many=True).data
                    })
        else:
            posts = Post.objects.all()
            return Response({
                "posts": PostSerializer(posts, many=True).data
                })

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            Post.objects.create(
                title=request.data['title'],
                content=request.data['content'],
                author=request.user
            )
            posts = Post.objects.filter(author=request.user)
            return Response({"posts": PostSerializer(posts, many=True).data})
        else: 
            return Response({
                "massage": "User not authorized."
                })

    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if request.user.is_authenticated:
            if post.author == request.user:
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response({
                    "massage": "Error data or bad request."
                    })
            else:
                return Response({
                    "massage": "This is post can't be delete, you are not the author."
                    })
        else:
            return Response({
                "massage": "User not authorized."
                })

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        if request.user.is_authenticated:
            if post.author == request.user:
                post.delete()
                return Response({
                    "massage": "Done. Deleted successfully"
                    })
            else:
                return Response({
                    "massage": "This is post can't be delete, you are not the author."
                    })
        else:
            return Response({
                "massage": "User not authorized."
                })


