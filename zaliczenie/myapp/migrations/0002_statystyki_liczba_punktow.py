# Generated by Django 4.2.16 on 2025-02-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statystyki',
            name='liczba_punktow',
            field=models.IntegerField(default=0),
        ),
    ]
