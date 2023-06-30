from rest_framework.views import APIView
from rest_framework import status, viewsets, parsers
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import PostSerializer
from .models import *
from django.views import View
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import Image



class PostViewSet(viewsets.ModelViewSet):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]
    
    def get_queryset(self):
        return Post.objects.filter(author_id=self.request.user.id)
    
    def get_serializer_class(self):
        return PostSerializer


    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = Post.objects.filter(author=user)
    #     return queryset
    # def get_queryset(self):
    #     user_id = self.kwargs["author_id"]
    #     return Post.objects.filter(user_id=user_id)
    
    # def create(self, request, *args, **kwargs):
    #     image_file = request.data.get('image')
    #     if image_file:
    #         image = Image.open(image_file)
            
    #         image.save(image_file.file, format='JPEG')
    #     return super().create(request, *args, **kwargs)

    
 

