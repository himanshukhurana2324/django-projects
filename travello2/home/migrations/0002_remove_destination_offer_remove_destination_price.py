# Generated by Django 5.0 on 2024-01-01 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='price',
        ),
    ]
