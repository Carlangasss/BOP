# Generated by Django 4.2.5 on 2023-09-25 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_horariouso_tipodispositivo_tiposector'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='idUsuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.usuario'),
        ),
    ]