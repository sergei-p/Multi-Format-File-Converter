# Generated by Django 2.0.7 on 2019-12-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JpegToPdf', '0010_pdf_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='JpegToPdf/original/'),
        ),
    ]
