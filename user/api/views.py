from rest_framework import permissions
from user.models import User
from user.api.serializers import UserSerializer
from rest_framework import viewsets
#from rest_framework.authentication import SessionAuthentication
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializers_class = UserSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticatedOrReadOnly]