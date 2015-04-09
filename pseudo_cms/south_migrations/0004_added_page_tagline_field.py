# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Content.page_tagline'
        db.add_column('pseudo_cms_content', 'page_tagline',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True),
                      keep_default=False)

        # Adding index on 'Content', fields ['url']
        db.create_index('pseudo_cms_content', ['url'])

    def backwards(self, orm):
        # Removing index on 'Content', fields ['url']
        db.delete_index('pseudo_cms_content', ['url'])

        # Deleting field 'Content.page_tagline'
        db.delete_column('pseudo_cms_content', 'page_tagline')

    models = {
        'pseudo_cms.content': {
            'Meta': {'ordering': "('url',)", 'object_name': 'Content'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_html': ('django.db.models.fields.TextField', [], {}),
            'content_format': ('django.db.models.fields.CharField', [], {'default': "u'text'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('image_helper.fields.SizedImageField', [], {'max_length': '100', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'page_tagline': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'page_title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['pseudo_cms']