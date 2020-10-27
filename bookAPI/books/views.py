from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='comedy')
    serializer_class = BookSerializer


class RomViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='romantic')
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='horror')
    serializer_class = BookSerializer


class AdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='adventure')
    serializer_class = BookSerializer


class MilitaryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='military')
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fantasy')
    serializer_class = BookSerializer


class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fiction')
    serializer_class = BookSerializer


class NonfictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='nonfiction')
    serializer_class = BookSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='history')
    serializer_class = BookSerializer


class ClassicViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='classic')
    serializer_class = BookSerializer





