# Generated by Django 4.2.1 on 2023-05-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_remove_sneakers_colour_alter_sneakers_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakers',
            name='colours',
            field=models.JSONField(default=[]),
        ),
    ]
