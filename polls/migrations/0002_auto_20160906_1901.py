# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160906134858 on 2016-09-06 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_examen_text', models.CharField(max_length=200)),
                ('motivo_text', models.CharField(max_length=200)),
                ('tension_ocular_text', models.CharField(max_length=200)),
                ('examen_ocular_text', models.CharField(max_length=200)),
                ('examen_compl_text', models.CharField(max_length=200)),
                ('tratamiento_text', models.CharField(max_length=200)),
                ('od_sin_lentes_text', models.CharField(max_length=200)),
                ('oi_sin_lentes_text', models.CharField(max_length=200)),
                ('od_con_lentes_text', models.CharField(max_length=200)),
                ('oi_con_lentes_text', models.CharField(max_length=200)),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_text', models.CharField(max_length=200)),
                ('apellido_text', models.CharField(max_length=200)),
                ('cedula_text', models.CharField(max_length=8)),
                ('nacimiento_date', models.DateTimeField(verbose_name='date published')),
                ('telefono_text', models.CharField(max_length=200)),
                ('direccion_text', models.CharField(max_length=200)),
                ('correo_text', models.CharField(max_length=200)),
                ('mutualista_text', models.CharField(max_length=200)),
                ('antecedentes_familiares_text', models.CharField(max_length=200)),
                ('antecedentes_personales_text', models.CharField(max_length=200)),
                ('otros_text', models.CharField(max_length=200)),
                ('historial_text', models.CharField(max_length=200)),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_receta_text', models.CharField(max_length=200)),
                ('historia_clinica_text', models.CharField(max_length=200)),
                ('lejos_od_text', models.CharField(max_length=200)),
                ('lejos_oi_text', models.CharField(max_length=200)),
                ('cerca_od_text', models.CharField(max_length=200)),
                ('cerca_oi_text', models.CharField(max_length=200)),
                ('add_text', models.CharField(max_length=200)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Paciente')),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.AddField(
            model_name='examen',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Paciente'),
        ),
    ]