from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import *
import jwt, datetime




# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
    

class UserView(APIView):
    def get(self, request):
        token =  request.COOKIES.get('access')
        
        if not token:
            raise AuthenticationFailed("Unauthenticated")
        
        try:
            payload =  jwt.decode(token, "secret", algorithms="HS256")
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token EXPIRED OR DELETED!")

        user = User.objects.filter(id=payload["id"]).first()
        serializer= UserSerializer(user)
        
        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()

        if(response): 
            response.delete_cookie("jwt")
            response.data = {
                "Successfully logged out"
        }
        else:
            response.data = {"User has not logged in. No cookie to be deleted"}
        
        return response
    


