# Generated by Django 3.0.3 on 2020-03-02 14:43

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200225_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieGenreTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(db_index=True, help_text='The registered model identifier.', max_length=100, verbose_name='identifier')),
                ('object_id', models.IntegerField(db_index=True, help_text='The object ID of this translation', verbose_name='The object ID')),
                ('language', models.CharField(choices=[('en', 'English'), ('fr', 'French')], db_index=True, default='en-us', help_text='The language for this translation', max_length=10, verbose_name='language')),
                ('field_name', models.CharField(db_index=True, help_text='The model field name for this translation.', max_length=100, verbose_name='field name')),
                ('field_value', models.TextField(help_text='The translated content for the field.', null=True, verbose_name='field value')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MovieTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(db_index=True, help_text='The registered model identifier.', max_length=100, verbose_name='identifier')),
                ('object_id', models.IntegerField(db_index=True, help_text='The object ID of this translation', verbose_name='The object ID')),
                ('language', models.CharField(choices=[('en', 'English'), ('fr', 'French')], db_index=True, default='en-us', help_text='The language for this translation', max_length=10, verbose_name='language')),
                ('field_name', models.CharField(db_index=True, help_text='The model field name for this translation.', max_length=100, verbose_name='field name')),
                ('field_value', models.TextField(help_text='The translated content for the field.', null=True, verbose_name='field value')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'movie', 'verbose_name_plural': 'movies'},
        ),
        migrations.AlterModelOptions(
            name='moviegenre',
            options={'verbose_name': 'movie genre', 'verbose_name_plural': 'movie genres'},
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='slug',
            new_name='slug_en',
        ),
        migrations.RenameField(
            model_name='moviegenre',
            old_name='slug',
            new_name='slug_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='country',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='synopsis',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.RemoveField(
            model_name='moviegenre',
            name='label',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='actors_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='country_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='country_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='director_en',
            field=models.CharField(max_length=100, null=True, verbose_name='director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director_fr',
            field=models.CharField(max_length=100, null=True, verbose_name='director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='slug_fr',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, null=True, populate_from='title'),
        ),
        migrations.AddField(
            model_name='movie',
            name='synopsis_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='synopsis_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='title_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviegenre',
            name='label_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviegenre',
            name='label_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviegenre',
            name='slug_fr',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='label'),
        ),
    ]
