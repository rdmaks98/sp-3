# Generated by Django 3.2.4 on 2021-09-01 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0002_auto_20210901_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addpropertyform',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='addpropertyform',
            name='county',
        ),
    ]
