# Generated by Django 4.2.2 on 2023-06-20 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_sneakers_colours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(default='', max_length=3000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
