from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import KlubPilkarski, Zawodnik, Trener, Mecz, Statystyki
from .serializers import KlubPilkarskiSerializer, ZawodnikSerializer, TrenerSerializer, MeczSerializer, StatystykiSerializer

class KlubPilkarskiViewSet(viewsets.ModelViewSet):
    queryset = KlubPilkarski.objects.all()
    serializer_class = KlubPilkarskiSerializer

class ZawodnikViewSet(viewsets.ModelViewSet):
    queryset = Zawodnik.objects.all()
    serializer_class = ZawodnikSerializer

class TrenerViewSet(viewsets.ModelViewSet):
    queryset = Trener.objects.all()
    serializer_class = TrenerSerializer

class MeczViewSet(viewsets.ModelViewSet):
    queryset = Mecz.objects.all()
    serializer_class = MeczSerializer

class StatystykiViewSet(viewsets.ModelViewSet):
    queryset = Statystyki.objects.all()
    serializer_class = StatystykiSerializer
