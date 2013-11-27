from django.db import models

# Create your models here.

class Station(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=256)
    lon = models.FloatField()
    lat = models.FloatField()
    line_code_1 = models.CharField(max_length=2)
    line_code_2 = models.CharField(max_length=2, blank=True, null=True)
    line_code_3 = models.CharField(max_length=2, blank=True, null=True)
    line_code_4 = models.CharField(max_length=2, blank=True, null=True)
    station_together_1 = models.CharField(max_length=3, blank=True, null=True)
    station_together_2 = models.CharField(max_length=3, blank=True, null=True)


class Confirmation(models.Model):
    tweet_text = models.CharField(max_length=256)
    time = models.BigIntegerField()
    status_id = models.CharField(max_length=256)


class Incident(models.Model):
    station = models.ForeignKey(Station)
    time_initially_reported = models.BigIntegerField()
    time_confirmed = models.BigIntegerField(blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    confirmation = models.ForeignKey(Confirmation, blank=True, null=True)


class Tweet(models.Model):
    """ Some links are long """
    tweet_text = models.CharField(max_length=256)
    username = models.CharField(max_length=21)
    user_full_name = models.CharField(max_length=100)
    time = models.BigIntegerField()
    status_id = models.CharField(max_length=256)
    incident_reporting = models.ForeignKey(Incident, blank=True, null=True)