# Generated by Django 2.2.5 on 2019-09-16 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Videonun basligi')),
                ('description', models.TextField(verbose_name='Text field')),
                ('video_path', models.FileField(upload_to='video_files/')),
                ('cover', models.ImageField(upload_to='video_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
