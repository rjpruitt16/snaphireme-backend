from django.contrib.auth.models import User
from api.models import SnapCapsule
from rest_framework import viewsets
from api.serializers import UserSerializer, SnapCapsuleSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnapCapsuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SnapCapsule.objects.all()
    serializer_class = SnapCapsuleSerializer
