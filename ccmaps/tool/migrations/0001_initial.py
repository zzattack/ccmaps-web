# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProgramVersion'
        db.create_table(u'tool_programversion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('release_date', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('release_notes', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('version', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'tool', ['ProgramVersion'])


    def backwards(self, orm):
        # Deleting model 'ProgramVersion'
        db.delete_table(u'tool_programversion')


    models = {
        u'tool.programversion': {
            'Meta': {'object_name': 'ProgramVersion'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'release_notes': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'version': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['tool']