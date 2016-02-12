# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
import django


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Robot'
        db.create_table('robot_robot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 9, 20, 0, 0))),
            ('time', self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2012, 9, 20, 0, 0))),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('robot', ['Robot'])

        # Adding model 'MotorType'
        db.create_table('robot_motortype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('robot', ['MotorType'])

        # Adding model 'Slot'
        db.create_table('robot_slot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('robot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['robot.Robot'])),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['robot.MotorType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('robot', ['Slot'])

        # Adding model 'Location'
        db.create_table('robot_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('robot', ['Location'])

        # Adding model 'State'
        db.create_table('robot_state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('robot', ['State'])

        # Adding model 'Motor'
        db.create_table('robot_motor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['robot.MotorType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('robot', ['Motor'])

        # Adding model 'MotorEvent'
        db.create_table('robot_motorevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['robot.Motor'])),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['robot.State'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 9, 20, 0, 0))),
            ('time', self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2012, 9, 20, 0, 0))),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('robot', ['MotorEvent'])

        # Adding model 'Association'
        db.create_table('robot_association', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['robot.Motor'])),
            ('slot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['robot.Slot'])),
            ('start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 9, 20, 0, 0))),
            ('start_time', self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2012, 9, 20, 0, 0))),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('end_time', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('robot', ['Association'])


    def backwards(self, orm):
        # Deleting model 'Robot'
        db.delete_table('robot_robot')

        # Deleting model 'MotorType'
        db.delete_table('robot_motortype')

        # Deleting model 'Slot'
        db.delete_table('robot_slot')

        # Deleting model 'Location'
        db.delete_table('robot_location')

        # Deleting model 'State'
        db.delete_table('robot_state')

        # Deleting model 'Motor'
        db.delete_table('robot_motor')

        # Deleting model 'MotorEvent'
        db.delete_table('robot_motorevent')

        # Deleting model 'Association'
        db.delete_table('robot_association')


    models = {
        'robot.association': {
            'Meta': {'object_name': 'Association'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['robot.Motor']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['robot.Slot']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 9, 20, 0, 0)'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2012, 9, 20, 0, 0)'})
        },
        'robot.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'robot.motor': {
            'Meta': {'object_name': 'Motor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['robot.MotorType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'robot.motorevent': {
            'Meta': {'object_name': 'MotorEvent'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 9, 20, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['robot.Motor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['robot.State']"}),
            'time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2012, 9, 20, 0, 0)'})
        },
        'robot.motortype': {
            'Meta': {'object_name': 'MotorType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'})
        },
        'robot.robot': {
            'Meta': {'object_name': 'Robot'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 9, 20, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2012, 9, 20, 0, 0)'})
        },
        'robot.slot': {
            'Meta': {'object_name': 'Slot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['robot.MotorType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'robot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['robot.Robot']"})
        },
        'robot.state': {
            'Meta': {'object_name': 'State'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['robot']
