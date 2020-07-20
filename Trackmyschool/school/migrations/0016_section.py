# Generated by Django 2.2.6 on 2019-10-14 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.AutoField(primary_key=True, serialize=False)),
                ('section_name', models.CharField(max_length=50, verbose_name='Section Name')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Class')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.SchoolsDetail')),
            ],
        ),
    ]
