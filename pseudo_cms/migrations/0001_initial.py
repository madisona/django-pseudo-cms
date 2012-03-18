# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Content'
        db.create_table('pseudo_cms_content', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('page_title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('image_helper.fields.SizedImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('pseudo_cms', ['Content'])


    def backwards(self, orm):
        
        # Deleting model 'Content'
        db.delete_table('pseudo_cms_content')


    models = {
        'pseudo_cms.content': {
            'Meta': {'ordering': "('url',)", 'object_name': 'Content'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('image_helper.fields.SizedImageField', [], {'max_length': '100', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'page_title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['pseudo_cms']
