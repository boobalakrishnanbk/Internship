# Generated by Django 2.2.6 on 2019-10-18 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0034_auto_20191018_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Class'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='exam_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.Exam'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Section'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='staff_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.AssignSubjectTeacher'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject'),
        ),
    ]
