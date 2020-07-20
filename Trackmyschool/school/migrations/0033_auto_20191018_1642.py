# Generated by Django 2.2.6 on 2019-10-18 11:12

from django.db import migrations, models
import school.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0032_auto_20191018_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='class_id',
            field=models.CharField(max_length=50, verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='exam_id',
            field=models.CharField(max_length=50, null=True, verbose_name=school.models.Exam),
        ),
        migrations.AlterField(
            model_name='mark',
            name='mark',
            field=models.CharField(max_length=50, verbose_name='Mark'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='section_id',
            field=models.CharField(max_length=50, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='staff_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Teacher'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject_id',
            field=models.CharField(max_length=50, verbose_name='Subject'),
        ),
    ]