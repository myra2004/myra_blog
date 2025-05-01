from django.urls import path

from posts.apis import PostListAPIView, PostDetailAPIView, PostCreateAPIView
from posts import views
from posts.views import HelloWorldView

urlpatterns = [
    path('all/', PostListAPIView.as_view()),
    path('<int:pk>/', PostDetailAPIView.as_view()),
    path('create/', PostCreateAPIView.as_view()),

    path('hello/', HelloWorldView.as_view(), name="hello_world"),
]