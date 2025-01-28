from django.contrib import admin
from .models import KlubPilkarski, Zawodnik, Trener, Mecz, Statystyki

admin.site.register(KlubPilkarski)
admin.site.register(Zawodnik)
admin.site.register(Trener)
admin.site.register(Mecz)
admin.site.register(Statystyki)
