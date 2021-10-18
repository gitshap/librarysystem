# Generated by Django 3.2.7 on 2021-10-18 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title_proper', models.CharField(max_length=255)),
                ('responsibility', models.CharField(max_length=255)),
                ('preferred_title', models.CharField(max_length=255)),
                ('parallel_title', models.CharField(max_length=255)),
                ('main_creator', models.CharField(max_length=255)),
                ('added_entry_creator', models.CharField(max_length=255)),
                ('contributors', models.CharField(max_length=255)),
                ('added_entry_corporate', models.CharField(max_length=255)),
                ('place_of_publication', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=255)),
                ('extent_of_text', models.CharField(max_length=255)),
                ('dimension', models.CharField(max_length=10)),
                ('series', models.CharField(max_length=10)),
                ('supplementary_content', models.CharField(choices=[('Choice 1', 'Choice 1'), ('Choice 2', 'Choice 2'), ('Choice 3', 'Choice 3')], default='Choice 1', max_length=10)),
                ('content_type', models.CharField(choices=[('Choice 1', 'Choice 1'), ('Choice 2', 'Choice 2'), ('Choice 3', 'Choice 3')], default='Choice 1', max_length=10)),
                ('media_type', models.CharField(choices=[('Choice 1', 'Choice 1'), ('Choice 2', 'Choice 2'), ('Choice 3', 'Choice 3')], default='Choice 1', max_length=10)),
                ('carrier_type', models.CharField(choices=[('Choice 1', 'Choice 1'), ('Choice 2', 'Choice 2'), ('Choice 3', 'Choice 3')], default='Choice 1', max_length=10)),
                ('identifier_isbn', models.CharField(max_length=11)),
                ('url', models.CharField(max_length=255)),
                ('call_number', models.CharField(choices=[('Choice 1', 'Choice 1'), ('Choice 2', 'Choice 2'), ('Choice 3', 'Choice 3')], default='Choice 2', max_length=10)),
                ('accession', models.CharField(max_length=255)),
                ('language', models.CharField(choices=[('Choice 1', 'Choice 1'), ('Choice 2', 'Choice 2'), ('Choice 3', 'Choice 3')], default='Choice 1', max_length=10)),
                ('library_location', models.CharField(choices=[('Choice 1', 'Choice 1'), ('Choice 2', 'Choice 2'), ('Choice 3', 'Choice 3')], default='Choice 1', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
