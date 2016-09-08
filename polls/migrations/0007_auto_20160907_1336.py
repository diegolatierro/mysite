# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160906134858 on 2016-09-07 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160907_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='antecedentes_familiares_text',
            new_name='antecedentes_familiares',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='antecedentes_personales_text',
            new_name='antecedentes_personales',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='cedula_text',
            new_name='cedula',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='correo_text',
            new_name='correo_electronico',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='direccion_text',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='historial_text',
            new_name='historial',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='mutualista_text',
            new_name='mutualista',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='otros_text',
            new_name='otros',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='telefono_text',
            new_name='telefono',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nacimiento_date',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
    ]