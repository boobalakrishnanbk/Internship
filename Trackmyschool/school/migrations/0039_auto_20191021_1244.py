# Generated by Django 2.2.6 on 2019-10-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0038_auto_20191021_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='mark',
            field=models.IntegerField(null=True, verbose_name='Mark'),
        ),
    ]