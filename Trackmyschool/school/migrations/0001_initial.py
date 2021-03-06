# Generated by Django 2.2.6 on 2019-10-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schools_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('fax', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=52)),
                ('zipcode', models.CharField(max_length=6)),
                ('website', models.URLField()),
                ('affillicateno', models.CharField(max_length=100)),
                ('logo', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
