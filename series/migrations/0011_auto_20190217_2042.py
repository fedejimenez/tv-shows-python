# Generated by Django 2.1.7 on 2019-02-17 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0010_tvshow_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tvshow',
            old_name='imdb',
            new_name='rating',
        ),
    ]