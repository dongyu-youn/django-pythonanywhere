# Generated by Django 2.2.5 on 2021-04-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_source', '0004_opensource_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='opensource',
            name='complet_error',
            field=models.BooleanField(default='False'),
        ),
    ]
