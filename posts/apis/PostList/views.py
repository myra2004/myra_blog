from rest_framework.views  import APIView
from rest_framework.response import Response

from posts.models import Post
from posts.apis.PostDetail.serializers import  PostListSerializer


class PostListAPIView(APIView):
    def get(self, request):
        print('>>>', request, request.data, request.user)
        posts = Post.objects.all()
        return Response({'posts': PostListSerializer(posts, many=True).data})