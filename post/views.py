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
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]
    
    # def create(self, request, *args, **kwargs):
    #     image_file = request.data.get('image')
    #     if image_file:
    #         image = Image.open(image_file)
            
    #         image.save(image_file.file, format='JPEG')
    #     return super().create(request, *args, **kwargs)

    
 

