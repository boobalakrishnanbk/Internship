# Generated by Django 2.2.6 on 2019-10-15 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0019_class_academic_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolSettings',
            fields=[
                ('settings_id', models.AutoField(primary_key=True, serialize=False)),
                ('academic_year', models.IntegerField(max_length=10, verbose_name='Academic Year')),
                ('pagination_count', models.IntegerField(max_length=100, verbose_name='Pagination Count')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.SchoolsDetail')),
            ],
        ),
    ]