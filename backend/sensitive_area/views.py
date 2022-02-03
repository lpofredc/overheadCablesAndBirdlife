from rest_framework import viewsets

from .models import SensitiveArea
from .serializers import SensitiveAreaSerializer

# from rest_framework.permissions import IsAuthenticated


class SensitiveAreaViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the SensitiveArea items"""

    serializer_class = SensitiveAreaSerializer
    # permission_classes = [IsAuthenticated]
    queryset = SensitiveArea.objects.all()
