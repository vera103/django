# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(default=datetime.datetime(2017, 10, 13, 10, 18, 18, 353745, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
