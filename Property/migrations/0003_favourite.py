# Generated by Django 3.2.4 on 2021-09-07 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Property', '0002_alter_agency_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='favourite',
            fields=[
                ('fid', models.IntegerField(primary_key=True, serialize=False)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.addpropertyform')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
