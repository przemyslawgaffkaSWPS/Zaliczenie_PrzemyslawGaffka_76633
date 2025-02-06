from django.db import models

class KlubPilkarski(models.Model):
    nazwa = models.CharField(max_length=50)
    miasto = models.CharField(max_length=40)
    rok_zalozenia = models.IntegerField()
    liga = models.CharField(max_length=50, choices=[
        ("Ekstraklasa", "Ekstraklasa"),
        ("I Liga", "I Liga"),
        ("II Liga", "II Liga"),
        ("III Liga", "III Liga"),
        ("IV Liga", "IV Liga"),
        ("Liga Okregowa", "Liga Okregowa"),
        ("A Klasa", "A Klasa"),
        ("B Klasa", "B Klasa")
    ])

    def __str__(self):
        return self.nazwa


class Zawodnik(models.Model):
    imie = models.CharField(max_length=15)
    nazwisko = models.CharField(max_length=15)
    data_urodzenia = models.DateField()
    narodowosc = models.CharField(max_length=15)
    przynaleznosc_klubowa = models.ForeignKey(KlubPilkarski, on_delete=models.CASCADE, related_name="zawodnicy")
    pozycja = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Trener(models.Model):
    imie = models.CharField(max_length=15)
    nazwisko = models.CharField(max_length=15)
    trener_klubu = models.ForeignKey(KlubPilkarski, on_delete=models.CASCADE, related_name="trener")

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Mecz(models.Model):
    druzyna_gospodarzy = models.ForeignKey(KlubPilkarski, on_delete=models.CASCADE, related_name="mecze_gospodarze")
    druzyna_gosci = models.ForeignKey(KlubPilkarski, on_delete=models.CASCADE, related_name="mecze_goscie")
    liczba_goli_gospodarzy = models.IntegerField()
    liczba_goli_gosci = models.IntegerField()
    data_meczu = models.DateField()
    zawodnik_meczu = models.ForeignKey(Zawodnik, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.druzyna_gospodarzy} vs {self.druzyna_gosci} z dnia {self.data_meczu}"


class Statystyki(models.Model):
    klub = models.OneToOneField(KlubPilkarski, on_delete=models.CASCADE, related_name="statystyki")
    liczba_punktow = models.IntegerField(default=0)
    liczba_meczow = models.IntegerField(default=0)
    mecze_wygrane = models.IntegerField(default=0)
    mecze_zremisowane = models.IntegerField(default=0)
    mecze_przegrane = models.IntegerField(default=0)
    bramki_strzelone = models.IntegerField(default=0)
    bramki_stracone = models.IntegerField(default=0)
    

    def __str__(self):
        return f"Statystyki {self.klub.nazwa}"
