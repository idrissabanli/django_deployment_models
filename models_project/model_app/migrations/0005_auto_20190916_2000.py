# Generated by Django 2.2.5 on 2019-09-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0004_auto_20190916_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='gender',
            field=models.CharField(choices=[('k', 'Kisi'), ('q', 'Qadin')], max_length=1, verbose_name='Cinsi'),
        ),
        migrations.AlterModelTable(
            name='blogger',
            table='bloggerler_siyahisi',
        ),
    ]
