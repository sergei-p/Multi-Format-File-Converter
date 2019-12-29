# Generated by Django 2.0.7 on 2019-12-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jpeg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=100, null=True)),
                ('image_file', models.FileField(null=True, upload_to='PngToJpeg/converted/')),
                ('cover', models.FileField(blank=True, null=True, upload_to='PngToJpeg/original/')),
            ],
        ),
        migrations.CreateModel(
            name='Png',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=100, null=True)),
                ('image_file', models.FileField(null=True, upload_to='PngToJpeg/original/')),
            ],
        ),
    ]
