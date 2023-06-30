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

 

