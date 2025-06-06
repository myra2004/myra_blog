from rest_framework.views  import APIView
from rest_framework.response import Response

from posts.models import Post
from posts.apis.PostDetail.serializers import  PostListSerializer


class PostDetailAPIView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return Response({'post': PostListSerializer(post).data})