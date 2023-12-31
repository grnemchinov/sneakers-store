# Generated by Django 4.2.1 on 2023-05-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_sneakers_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakers',
            name='note',
            field=models.TextField(default='', max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='sneakers',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Мужской'), (1, 'Женский')], default=0, null=True),
        ),
    ]
