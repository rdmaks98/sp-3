# Generated by Django 3.2.4 on 2021-07-13 06:47

import datetime
from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('mobile', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('profile', models.ImageField(default='', upload_to='Property/images/profile')),
                ('user_type', models.CharField(choices=[('user', 'user'), ('broker', 'broker')], default='user', max_length=10)),
                ('details', models.CharField(max_length=200)),
                ('dob', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.DeleteModel(
            name='Broker',
        ),
    ]