# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Can be let blank for little items like motors', max_length=70, blank=True)),
                ('description', models.TextField(help_text=b'Additional information about this item', null=True, blank=True)),
                ('image', models.FileField(null=True, upload_to=b'%Y/%m/%d', blank=True)),
                ('price', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('parent_item', models.ForeignKey(blank=True, to='resources.Item', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'active')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'creation date')),
                ('last_modification_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'last modification date')),
                ('passived_date', models.DateTimeField(default=None, help_text=b'Date were this state became inactive. Automatically set when the is_active field become unchecked.', null=True, verbose_name=b'passived date', blank=True)),
                ('description', models.TextField(help_text=b'Additional information about this state', null=True, blank=True)),
                ('priority', models.IntegerField(default=1, help_text=b'Priority of the loan. Only staff renter should have high priority', choices=[(0, b'Low'), (1, b'Normal'), (3, b'High')])),
                ('starting_date', models.DateTimeField(help_text=b'Starting date of the loan', verbose_name=b'loan starting date')),
                ('ending_date', models.DateTimeField(help_text=b'Ending date of the loan', verbose_name=b'loan ending date')),
                ('creator', models.ForeignKey(related_name='loan_event_created', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, help_text=b'User who create this event', null=True)),
                ('items', models.ManyToManyField(help_text=b'Items loaned by an user', to='resources.Item')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, help_text=b'User who borrow the Item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.FileField(null=True, upload_to=b'%Y/%m/%d', blank=True)),
                ('category', models.ForeignKey(to='resources.Category')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'active')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'creation date')),
                ('last_modification_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'last modification date')),
                ('passived_date', models.DateTimeField(default=None, help_text=b'Date were this state became inactive. Automatically set when the is_active field become unchecked.', null=True, verbose_name=b'passived date', blank=True)),
                ('description', models.TextField(help_text=b'Additional information about this state', null=True, blank=True)),
                ('working_state', models.CharField(default=b'OK', max_length=2, choices=[(b'OK', b'Works well'), (b'HS', b'Broken'), (b'RE', b'In reparation'), (b'TC', b'Undetermined')])),
                ('creator', models.ForeignKey(related_name='state_event_created', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, help_text=b'User who create this event', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='item',
            name='reference',
            field=models.ForeignKey(to='resources.Reference'),
        ),
    ]
