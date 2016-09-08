# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160906134858 on 2016-09-07 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20160907_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examen',
            old_name='examen_ocular_text',
            new_name='examen_ocular',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='examen_compl_text',
            new_name='examenes_complementarios',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='motivo_text',
            new_name='motivo',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='od_con_lentes_text',
            new_name='od_con_lentes',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='od_sin_lentes_text',
            new_name='od_sin_lentes',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='oi_con_lentes_text',
            new_name='oi_con_lentes',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='oi_sin_lentes_text',
            new_name='oi_sin_lentes',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='tension_ocular_text',
            new_name='tension_ocular',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='tratamiento_text',
            new_name='tratamiento',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='add_text',
            new_name='add',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='cerca_od_text',
            new_name='cerca_od',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='cerca_oi_text',
            new_name='cerca_oi',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='historia_clinica_text',
            new_name='historia_clinica',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='lejos_od_text',
            new_name='lejos_od',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='lejos_oi_text',
            new_name='lejos_oi',
        ),
        migrations.AlterField(
            model_name='examen',
            name='fecha_examen_text',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha examen'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='fecha_receta_text',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha receta'),
        ),
    ]