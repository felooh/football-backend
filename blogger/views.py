from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import *
import jwt, datetime
from rest_framework.generics import  UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound





# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        

class GetLoggedInUser(RetrieveAPIView):
    # permission_classes = (IsAuthenticated)
    serializer_class = UserSerializer
    queryset = User.objects.all()  # Specify the queryset to update

    
    def get_object(self):
        return self.request.user
    
class UpdateUser(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()  # Specify the queryset to update

    
    def get_object(self):
        user = self.request.user

        if user.is_authenticated:
            return user
        else:
            return None
    

       


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
    


