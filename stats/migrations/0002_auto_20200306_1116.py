# Generated by Django 3.0.3 on 2020-03-06 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='visitstat',
            unique_together={('url', 'IP', 'date')},
        ),
    ]
