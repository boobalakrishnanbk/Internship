# Generated by Django 2.2.6 on 2019-10-14 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_staffdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetail',
            name='emergency_number',
            field=models.CharField(max_length=20, verbose_name='Emergency Number'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='mobile',
            field=models.CharField(max_length=20, verbose_name='Mobile Number'),
        ),
    ]
