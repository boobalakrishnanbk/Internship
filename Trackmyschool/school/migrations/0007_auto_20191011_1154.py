# Generated by Django 2.2.6 on 2019-10-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_schoolsdetail_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolsdetail',
            name='usertype',
            field=models.CharField(default='admin', max_length=50, null=True, verbose_name='User Type'),
        ),
    ]
