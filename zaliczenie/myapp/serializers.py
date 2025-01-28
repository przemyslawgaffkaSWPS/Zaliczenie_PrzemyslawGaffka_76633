from rest_framework import serializers
from .models import KlubPilkarski, Zawodnik, Trener, Mecz, Statystyki

class KlubPilkarskiSerializer(serializers.ModelSerializer):
    class Meta:
        model = KlubPilkarski
        fields = '__all__'

class ZawodnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zawodnik
        fields = '__all__'

class TrenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trener
        fields = '__all__'

class MeczSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mecz
        fields = '__all__'

class StatystykiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statystyki
        fields = '__all__'
