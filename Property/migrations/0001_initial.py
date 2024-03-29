# Generated by Django 3.2.4 on 2021-09-06 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddPropertyForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyTitle', models.CharField(max_length=255)),
                ('propertyType', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('propertyDescription', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('Neighborhood', models.CharField(max_length=255)),
                ('areasize', models.CharField(max_length=255)),
                ('sizeprefix', models.CharField(max_length=255)),
                ('landarea', models.CharField(max_length=255)),
                ('landAreaSize', models.CharField(max_length=255)),
                ('bedrooms', models.CharField(max_length=255)),
                ('bathrooms', models.CharField(max_length=255)),
                ('builtyear', models.CharField(max_length=255)),
                ('propertyimage', models.ImageField(default='', upload_to='Property/images/property')),
            ],
        ),
        migrations.CreateModel(
            name='BrokerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('mobile', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('profile', models.ImageField(upload_to='Property/images/profile')),
                ('user_type', models.CharField(choices=[('user', 'user'), ('broker', 'broker')], default='user', max_length=10)),
                ('details', models.CharField(max_length=200)),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('Rid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('rate', models.IntegerField()),
                ('review', models.CharField(max_length=255)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.addpropertyform')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('ctid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=255)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BrokerSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=255)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.brokercategory')),
            ],
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('a_name', models.CharField(default='', max_length=200)),
                ('a_image', models.ImageField(default='', upload_to='Property/images/agency/')),
                ('a_address', models.CharField(default='', max_length=200)),
                ('u_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='addpropertyform',
            name='cate_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Property.brokercategory'),
        ),
        migrations.AddField(
            model_name='addpropertyform',
            name='subcate_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Property.brokersubcategory'),
        ),
    ]
