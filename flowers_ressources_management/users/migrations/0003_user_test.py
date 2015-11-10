# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151104_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.CharField(verbose_name='Test', blank=True, max_length=255),
        ),
    ]
