# Generated by Django 3.0.3 on 2020-02-25 11:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movie_rented'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, null=True, populate_from='title'),
        ),
    ]
