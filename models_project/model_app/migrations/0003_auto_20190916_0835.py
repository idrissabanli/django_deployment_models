# Generated by Django 2.2.5 on 2019-09-16 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0002_auto_20190916_0833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogger',
            options={'ordering': ('-nickname',), 'verbose_name': 'Blogger', 'verbose_name_plural': 'Bloggerler siyahisi'},
        ),
    ]
