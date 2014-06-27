# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Evento'
        db.create_table('web_evento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('fecha_registro', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('web', ['Evento'])


    def backwards(self, orm):
        # Deleting model 'Evento'
        db.delete_table('web_evento')


    models = {
        'web.evento': {
            'Meta': {'object_name': 'Evento'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha_registro': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['web']