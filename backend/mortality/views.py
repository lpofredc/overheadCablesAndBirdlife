from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Mortality
from .serializers import MortalitySerializer


class MortalityViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the Mortality items"""

    serializer_class = MortalitySerializer
    permission_classes = [IsAuthenticated]
    queryset = Mortality.objects.all()
