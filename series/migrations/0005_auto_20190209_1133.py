# Generated by Django 2.1.5 on 2019-02-09 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_auto_20190209_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serie',
            old_name='location',
            new_name='description',
        ),
    ]