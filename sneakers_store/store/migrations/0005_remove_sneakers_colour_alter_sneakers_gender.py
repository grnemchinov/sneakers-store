# Generated by Django 4.2.1 on 2023-05-11 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_sneakers_note_alter_sneakers_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sneakers',
            name='colour',
        ),
        migrations.AlterField(
            model_name='sneakers',
            name='gender',
            field=models.IntegerField(choices=[(0, 'male'), (1, 'female')], default=0, null=True),
        ),
    ]
