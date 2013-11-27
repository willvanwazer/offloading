# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
import requests
from offloading.api.models import Station, Confirmation, Incident, Tweet

class Migration(SchemaMigration):

    def forwards(self, orm):
        r = requests.get("https://raw.github.com/willvanwazer/metro-status-board/master/stations.json")
        for station_json in r.json():
            station = Station()
            station.code = station_json['Code']
            station.name = station_json['Name']
            station.lon = station_json['Lon']
            station.lat = station_json['Lat']
            station.line_code_1 = station_json['LineCode1']
            station.line_code_2 = station_json['LineCode2']
            station.line_code_3 = station_json['LineCode3']
            station.line_code_4 = station_json['LineCode4']
            station.station_together_1 = station_json['StationTogether1']
            station.station_together_2 = station_json['StationTogether2']
            
            station.save()

    def backwards(self, orm):
        pass

    models = {
        u'api.confirmation': {
            'Meta': {'object_name': 'Confirmation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'time': ('django.db.models.fields.BigIntegerField', [], {}),
            'tweet_text': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'api.incident': {
            'Meta': {'object_name': 'Incident'},
            'confirmation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Confirmation']", 'null': 'True', 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Station']"}),
            'time_confirmed': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_initially_reported': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'api.station': {
            'Meta': {'object_name': 'Station'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'line_code_1': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'line_code_2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'line_code_3': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'line_code_4': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'station_together_1': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'station_together_2': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        u'api.tweet': {
            'Meta': {'object_name': 'Tweet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incident_reporting': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Incident']", 'null': 'True', 'blank': 'True'}),
            'status_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'time': ('django.db.models.fields.BigIntegerField', [], {}),
            'tweet_text': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user_full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '21'})
        }
    }

    complete_apps = ['api']