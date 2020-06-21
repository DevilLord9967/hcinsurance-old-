# Generated by Django 2.1.4 on 2018-12-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('benefits', models.TextField()),
                ('min_sum', models.IntegerField()),
                ('max_sum', models.IntegerField(blank=True)),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('min_payterm', models.IntegerField()),
                ('max_payterm', models.IntegerField()),
            ],
        ),
    ]