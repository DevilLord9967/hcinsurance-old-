# Generated by Django 2.1.4 on 2019-01-22 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20190122_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_policy',
            name='client_name',
        ),
        migrations.AlterField(
            model_name='reciept',
            name='client_name',
            field=models.ForeignKey(on_delete=True, to='client.Client'),
        ),
        migrations.DeleteModel(
            name='Client_Policy',
        ),
    ]
