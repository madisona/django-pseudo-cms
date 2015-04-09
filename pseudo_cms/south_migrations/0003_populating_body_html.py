# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

from pseudo_cms.utils import convert_to_html

class Migration(DataMigration):

    def forwards(self, orm):
        # saving will force the conversion of body content to body_html
        for c in orm.Content.objects.all():
            c.body_html = convert_to_html(c.body, c.content_format)
            c.save()


    def backwards(self, orm):
        "Write your backwards methods here."


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
    symmetrical = True
