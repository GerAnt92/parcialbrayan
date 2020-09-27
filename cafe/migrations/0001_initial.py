# Generated by Django 3.1.1 on 2020-09-27 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id_bodega', models.AutoField(primary_key=True, serialize=False)),
                ('encargado_bodega', models.CharField(max_length=100)),
                ('capacidad_bodega', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CentroAcopio',
            fields=[
                ('id_centro_acopio', models.AutoField(primary_key=True, serialize=False)),
                ('encargado_centro_acopio', models.CharField(max_length=100)),
                ('direccion_centro_acopio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('id_productor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_productor', models.CharField(max_length=100)),
                ('nombre_apellido', models.CharField(max_length=100)),
                ('direccion_productor', models.CharField(max_length=100)),
                ('telefono_productor', models.PositiveIntegerField()),
                ('correo_productor', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id_entrega', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_entrega', models.DateField()),
                ('importe_entrega', models.FloatField()),
                ('id_bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.bodega')),
                ('id_centro_acopio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.centroacopio')),
                ('id_productor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.productor')),
            ],
        ),
    ]