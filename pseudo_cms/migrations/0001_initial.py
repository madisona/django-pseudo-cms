# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pseudo_cms.validators
import image_helper.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(help_text=b'URL endpoint of page content belongs to.', unique=True, max_length=200, db_index=True, validators=[pseudo_cms.validators.internal_path_exists])),
                ('title', models.CharField(help_text=b'Title that shows on searches / browser tab.', max_length=100)),
                ('meta_description', models.CharField(help_text=b'Description that shows in search engine.', max_length=200)),
                ('page_title', models.CharField(help_text=b'Title that shows on page.', max_length=60)),
                ('page_tagline', models.CharField(help_text=b'Tagline / Subtitle for page', max_length=120, blank=True)),
                ('content_format', models.CharField(default='text', max_length=50, choices=[('html', 'Raw HTML'), ('reST', 'reStructuredText'), ('text', 'Plain Text')])),
                ('body', models.TextField()),
                ('body_html', models.TextField()),
                ('image', image_helper.fields.SizedImageField(upload_to=b'cms/content', blank=True)),
            ],
            options={
                'ordering': ('url',),
            },
            bases=(models.Model,),
        ),
    ]
