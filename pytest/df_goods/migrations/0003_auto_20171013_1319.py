# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_goodsinfo_gcontent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsinfo',
            old_name='gjanjie',
            new_name='gjianjie',
        ),
    ]
