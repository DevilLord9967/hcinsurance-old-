# Generated by Django 2.1.4 on 2019-01-22 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20181230_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_number', models.IntegerField()),
                ('policy_number', models.IntegerField()),
                ('paying_term', models.IntegerField()),
                ('maturity_term', models.IntegerField()),
                ('premium', models.IntegerField()),
                ('mode', models.CharField(max_length=20)),
                ('DOC', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='client',
            old_name='mobile',
            new_name='mobile1',
        ),
        migrations.RemoveField(
            model_name='client',
            name='DOC',
        ),
        migrations.RemoveField(
            model_name='client',
            name='maturity_term',
        ),
        migrations.RemoveField(
            model_name='client',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='client',
            name='paying_term',
        ),
        migrations.RemoveField(
            model_name='client',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='client',
            name='plan_number',
        ),
        migrations.RemoveField(
            model_name='client',
            name='policy_number',
        ),
        migrations.RemoveField(
            model_name='client',
            name='premium',
        ),
        migrations.AddField(
            model_name='client',
            name='mobile2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='reciept',
            name='image',
            field=models.ImageField(upload_to='Premium_Reciept/%Y-%m-%d/'),
        ),
        migrations.AddField(
            model_name='client_policy',
            name='client_name',
            field=models.ForeignKey(on_delete=False, to='client.Client'),
        ),
    ]