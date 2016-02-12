# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='test',
            field=models.CharField(max_length=255, verbose_name='test', blank=True),
        ),
    ]
