# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160906134858 on 2016-09-07 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20160907_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='apellido_text',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='nombre_text',
            new_name='nombre',
        ),
    ]