# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ID'
        db.create_table('content_id', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_valid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('content', ['ID'])


    def backwards(self, orm):
        
        # Deleting model 'ID'
        db.delete_table('content_id')


    models = {
        'content.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'content.film': {
            'Meta': {'object_name': 'Film', '_ormbases': ['content.MediaEntry']},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mediaentry_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['content.MediaEntry']", 'unique': 'True', 'primary_key': 'True'}),
            'tags': ('tagging.fields.TagField', [], {})
        },
        'content.id': {
            'Meta': {'object_name': 'ID'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'content.mediaentry': {
            'Meta': {'object_name': 'MediaEntry'},
            'emotions': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '400'})
        }
    }

    complete_apps = ['content']
