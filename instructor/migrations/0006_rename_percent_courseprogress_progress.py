# Generated by Django 5.0.3 on 2024-03-23 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0005_courseprogress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseprogress',
            old_name='percent',
            new_name='progress',
        ),
    ]
