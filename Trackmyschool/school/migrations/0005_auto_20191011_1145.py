# Generated by Django 2.2.6 on 2019-10-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20191011_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolsdetail',
            name='password',
            field=models.CharField(max_length=50, null=True, verbose_name='Password'),
        ),
        migrations.AddField(
            model_name='schoolsdetail',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Username'),
        ),
    ]
