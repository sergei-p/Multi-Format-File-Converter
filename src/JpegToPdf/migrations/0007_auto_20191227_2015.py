# Generated by Django 2.0.7 on 2019-12-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JpegToPdf', '0006_auto_20191227_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jpeg',
            name='image_file',
            field=models.FileField(null=True, upload_to='JpegToPdf/original/'),
        ),
    ]
