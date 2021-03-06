# Generated by Django 2.2.6 on 2019-10-15 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0022_auto_20191015_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignSubjectTeacher',
            fields=[
                ('assign_subject_teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('academic_year', models.CharField(max_length=20, verbose_name='Academic Year')),
                ('is_class_teacher', models.CharField(max_length=10, verbose_name='Class Teacher')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Class')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Section')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.StaffDetail')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject')),
            ],
        ),
    ]
