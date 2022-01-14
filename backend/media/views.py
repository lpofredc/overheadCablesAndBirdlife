from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Picture
from .serializers import PictureSerializer


class PictureViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Picture items"""

    serializer_class = PictureSerializer
    permission_classes = [IsAuthenticated]
    queryset = Picture.objects.all()
