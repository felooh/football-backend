from rest_framework.views import APIView
from rest_framework import status, viewsets, parsers
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import PostSerializer
from .models import *
from django.views import View
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import Image
from rest_framework.decorators import action



class PostViewSet(viewsets.ModelViewSet):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]

    def get_serializer_class(self):
        return PostSerializer

    def get_queryset(self):
        posts = Post.objects.all()
        return posts

    @action(methods=['get'], detail=False, url_path="all")
    def get_posts(self, request):
        posts = self.get_queryset()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path="author")
    def get_posts_by_author(self, request):
        posts = Post.objects.filter(author_id=self.request.user.id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





