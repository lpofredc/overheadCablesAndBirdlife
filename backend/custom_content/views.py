from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import News, Partners
from .serializers import (
    NewsFullSerializer,
    NewsSimpleSerializer,
    PartnersSerializer,
)


class NewsSimpleViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the news items"""

    serializer_class = NewsSimpleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = News.objects.all()


class NewsFullViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the News items with body"""

    serializer_class = NewsFullSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = News.objects.all()


class PartnersViewSet(viewsets.ModelViewSet):
    """A simple viewset to retrieve all the partners"""

    serializer_class = PartnersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Partners.objects.all()
