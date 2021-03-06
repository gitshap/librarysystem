# Generated by Django 3.2.7 on 2021-12-22 06:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0004_alter_book_accession'),
    ]

    operations = [
        migrations.AddField(
            model_name='acquisition',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acquisition',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='accession',
            field=models.CharField(max_length=255),
        ),
    ]
