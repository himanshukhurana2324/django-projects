# Generated by Django 5.0 on 2024-01-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_destination_offer_destination_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(),
        ),
    ]