# Generated by Django 2.1.7 on 2019-02-18 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0021_auto_20190218_0151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='tvshows',
            new_name='tvshow',
        ),
    ]