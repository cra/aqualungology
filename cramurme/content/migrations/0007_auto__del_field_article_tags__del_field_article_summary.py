# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Article.tags'
        db.delete_column('content_article', 'tags')

        # Deleting field 'Article.summary'
        db.delete_column('content_article', 'summary')


    def backwards(self, orm):
        
        # Adding field 'Article.tags'
        db.add_column('content_article', 'tags', self.gf('tagging.fields.TagField')(default=''), keep_default=False)

        # Adding field 'Article.summary'
        db.add_column('content_article', 'summary', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    models = {
        'content.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
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
