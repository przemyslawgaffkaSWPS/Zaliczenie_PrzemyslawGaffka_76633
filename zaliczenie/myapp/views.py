from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import KlubPilkarski, Zawodnik, Trener, Mecz, Statystyki
from .serializers import KlubPilkarskiSerializer, ZawodnikSerializer, TrenerSerializer, MeczSerializer, StatystykiSerializer

class KlubPilkarskiViewSet(viewsets.ModelViewSet):
    queryset = KlubPilkarski.objects.all()
    serializer_class = KlubPilkarskiSerializer

    @action(detail=False, methods=['get'])
    def ranking(self, request):
        kluby = KlubPilkarski.objects.all().order_by('-statystyki__liczba_punktow')
        serializer = self.get_serializer(kluby, many=True)
        return Response(serializer.data)

class ZawodnikViewSet(viewsets.ModelViewSet):
    queryset = Zawodnik.objects.all()
    serializer_class = ZawodnikSerializer

class TrenerViewSet(viewsets.ModelViewSet):
    queryset = Trener.objects.all()
    serializer_class = TrenerSerializer

class MeczViewSet(viewsets.ModelViewSet):
    queryset = Mecz.objects.all()
    serializer_class = MeczSerializer

    @action(detail=True, methods=['get'])
    def historia(self, request, pk=None):
        klub = self.get_object()
        mecze = Mecz.objects.filter(druzyna_gospodarzy=klub) | Mecz.objects.filter(druzyna_gosci=klub)
        serializer = self.get_serializer(mecze, many=True)
        return Response(serializer.data)

class StatystykiViewSet(viewsets.ModelViewSet):
    queryset = Statystyki.objects.all()
    serializer_class = StatystykiSerializer

def kluby(request):
    kluby = KlubPilkarski.objects.all()
    return render(request, 'kluby.html', {'kluby': kluby})