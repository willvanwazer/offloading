# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Station'
        db.create_table(u'api_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('lon', self.gf('django.db.models.fields.FloatField')()),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('line_code_1', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('line_code_2', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('line_code_3', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('line_code_4', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('station_together_1', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('station_together_2', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Station'])

        # Adding model 'Confirmation'
        db.create_table(u'api_confirmation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tweet_text', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('time', self.gf('django.db.models.fields.BigIntegerField')()),
            ('status_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'api', ['Confirmation'])

        # Adding model 'Incident'
        db.create_table(u'api_incident', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Station'])),
            ('time_initially_reported', self.gf('django.db.models.fields.BigIntegerField')()),
            ('time_confirmed', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('confirmation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Confirmation'], null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Incident'])

        # Adding model 'Tweet'
        db.create_table(u'api_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tweet_text', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=21)),
            ('user_full_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('time', self.gf('django.db.models.fields.BigIntegerField')()),
            ('status_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('incident_reporting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Incident'], null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Tweet'])


    def backwards(self, orm):
        # Deleting model 'Station'
        db.delete_table(u'api_station')

        # Deleting model 'Confirmation'
        db.delete_table(u'api_confirmation')

        # Deleting model 'Incident'
        db.delete_table(u'api_incident')

        # Deleting model 'Tweet'
        db.delete_table(u'api_tweet')


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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
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