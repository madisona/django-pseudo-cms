# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Content.content_format'
        db.add_column('pseudo_cms_content', 'content_format',
                      self.gf('django.db.models.fields.CharField')(default=u'text', max_length=50),
                      keep_default=False)

        # Adding field 'Content.body_html'
        db.add_column('pseudo_cms_content', 'body_html',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'Content.title'
        db.alter_column('pseudo_cms_content', 'title', self.gf('django.db.models.fields.CharField')(max_length=100))
    def backwards(self, orm):
        # Deleting field 'Content.content_format'
        db.delete_column('pseudo_cms_content', 'content_format')

        # Deleting field 'Content.body_html'
        db.delete_column('pseudo_cms_content', 'body_html')


        # Changing field 'Content.title'
        db.alter_column('pseudo_cms_content', 'title', self.gf('django.db.models.fields.CharField')(max_length=60))
    models = {
        'pseudo_cms.content': {
            'Meta': {'ordering': "('url',)", 'object_name': 'Content'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_html': ('django.db.models.fields.TextField', [], {}),
            'content_format': ('django.db.models.fields.CharField', [], {'default': "u'text'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('image_helper.fields.SizedImageField', [], {'max_length': '100', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'page_title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['pseudo_cms']