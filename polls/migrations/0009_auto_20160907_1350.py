# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160906134858 on 2016-09-07 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20160907_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examen',
            old_name='examenes_complementarios',
            new_name='examen_compl_text',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='examen_ocular',
            new_name='examen_ocular_text',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='motivo',
            new_name='motivo_text',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='od_con_lentes',
            new_name='od_con_lentes_text',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='od_sin_lentes',
            new_name='od_sin_lentes_text',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='oi_con_lentes',
            new_name='oi_con_lentes_text',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='oi_sin_lentes',
            new_name='oi_sin_lentes_text',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='tension_ocular',
            new_name='tension_ocular_text',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='tratamiento',
            new_name='tratamiento_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='antecedentes_familiares',
            new_name='antecedentes_familiares_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='antecedentes_personales',
            new_name='antecedentes_personales_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='apellido',
            new_name='apellido_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='cedula',
            new_name='cedula_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='correo_electronico',
            new_name='correo_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='direccion',
            new_name='direccion_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='historial',
            new_name='historial_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='mutualista',
            new_name='mutualista_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='nombre',
            new_name='nombre_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='otros',
            new_name='otros_text',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='telefono',
            new_name='telefono_text',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='add',
            new_name='add_text',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='cerca_od',
            new_name='cerca_od_text',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='cerca_oi',
            new_name='cerca_oi_text',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='historia_clinica',
            new_name='historia_clinica_text',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='lejos_od',
            new_name='lejos_od_text',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='lejos_oi',
            new_name='lejos_oi_text',
        ),
        migrations.AlterField(
            model_name='examen',
            name='fecha_examen_text',
            field=models.DateField(blank=True, null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nacimiento_date',
            field=models.DateField(verbose_name='Fecha de naciento'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='fecha_receta_text',
            field=models.DateField(blank=True, null=True, verbose_name='date published'),
        ),
    ]