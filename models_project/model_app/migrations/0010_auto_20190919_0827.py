# Generated by Django 2.2.5 on 2019-09-19 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0009_auto_20190919_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_app.Author', verbose_name='Mullif'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='content',
            field=models.TextField(verbose_name='Mezmun'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=20, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=40, verbose_name='ad, Soyad'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Movzu'),
        ),
    ]
