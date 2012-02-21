# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Article'
        db.create_table('content_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
        ))
        db.send_create_signal('content', ['Article'])

        # Adding model 'MediaEntry'
        db.create_table('content_mediaentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('reason', self.gf('django.db.models.fields.TextField')(default='', max_length=400)),
            ('processed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('emotions', self.gf('django.db.models.fields.TextField')(default='', max_length=300)),
        ))
        db.send_create_signal('content', ['MediaEntry'])

        # Adding model 'Film'
        db.create_table('content_film', (
            ('mediaentry_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.MediaEntry'], unique=True, primary_key=True)),
            ('length', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('content', ['Film'])


    def backwards(self, orm):
        
        # Deleting model 'Article'
        db.delete_table('content_article')

        # Deleting model 'MediaEntry'
        db.delete_table('content_mediaentry')

        # Deleting model 'Film'
        db.delete_table('content_film')


    models = {
        'content.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'content.film': {
            'Meta': {'object_name': 'Film', '_ormbases': ['content.MediaEntry']},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mediaentry_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['content.MediaEntry']", 'unique': 'True', 'primary_key': 'True'})
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
