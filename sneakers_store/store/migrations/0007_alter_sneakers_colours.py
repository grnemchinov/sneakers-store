# Generated by Django 4.2.1 on 2023-05-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_sneakers_colours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneakers',
            name='colours',
            field=models.JSONField(default=list),
        ),
    ]
