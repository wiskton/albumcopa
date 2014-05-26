# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Figurinha'
        db.create_table(u'figurinhas_figurinha', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('tenho', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'figurinhas', ['Figurinha'])


    def backwards(self, orm):
        # Deleting model 'Figurinha'
        db.delete_table(u'figurinhas_figurinha')


    models = {
        u'figurinhas.figurinha': {
            'Meta': {'object_name': 'Figurinha'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'tenho': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['figurinhas']