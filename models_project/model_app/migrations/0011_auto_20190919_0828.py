# Generated by Django 2.2.5 on 2019-09-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0010_auto_20190919_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=20, verbose_name='E poct'),
        ),
    ]
