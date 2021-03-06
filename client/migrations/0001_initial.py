# Generated by Django 2.1.4 on 2018-12-30 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateTimeField()),
                ('plan_number', models.IntegerField()),
                ('mobile', models.CharField(max_length=20)),
                ('policy_number', models.IntegerField()),
                ('paying_term', models.IntegerField()),
                ('maturity_term', models.IntegerField()),
                ('premium', models.IntegerField()),
                ('mode', models.CharField(max_length=20)),
                ('address', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='CL_photos/%Y/%m/%d/')),
                ('DOC', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reciept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='Premium_Reciept/%Y/%m/%d/')),
                ('user_email', models.ForeignKey(on_delete=False, to='client.Client')),
            ],
        ),
    ]
