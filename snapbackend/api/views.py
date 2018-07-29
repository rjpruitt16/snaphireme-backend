from django.contrib.auth.models import User
from api.models import SnapCapsule
from rest_framework import viewsets
from api.serializers import UserSerializer, SnapCapsuleSerializer
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from logging import info

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        info("User Action: ", self.action)
        if self.action in ['destroy', "list"]:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

class SnapCapsuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SnapCapsule.objects.all()
    serializer_class = SnapCapsuleSerializer

    def get_queryset(self):
        threshold = datetime.now() + timedelta(days=1)
        return self.queryset.filter(dateToDelete__range=[datetime.now(), threshold])

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        info("Capsule Action: ", self.action)
        if self.action == 'destroy':
            permission_classes = [IsAdminUser]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
