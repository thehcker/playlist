# Generated by Django 2.2 on 2019-05-07 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20190501_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='file_type',
            new_name='audio_file',
        ),
    ]
