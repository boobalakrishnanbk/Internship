# Generated by Django 2.2.6 on 2019-10-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0041_auto_20191021_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffdetail',
            name='bank_details',
        ),
        migrations.AlterField(
            model_name='schoolsdetail',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='schoolsdetail',
            name='country',
            field=models.CharField(default='India', max_length=100, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='schoolsdetail',
            name='logo',
            field=models.FileField(blank=True, upload_to='documents/', verbose_name='School Logo'),
        ),
        migrations.AlterField(
            model_name='schoolsdetail',
            name='state',
            field=models.CharField(default='Tamil Nadu', max_length=52, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='schoolsdetail',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='schoolsdetail',
            name='usertype',
            field=models.CharField(default='admin', max_length=50, verbose_name='User Type'),
        ),
        migrations.AlterField(
            model_name='schoolsdetail',
            name='website',
            field=models.URLField(blank=True, verbose_name='Website URL'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='Photo',
            field=models.FileField(blank=True, upload_to='user_image/', verbose_name='Staff Photo'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='Photo',
            field=models.FileField(blank=True, upload_to='user_image/', verbose_name='Student Photo'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='country',
            field=models.CharField(default='India', max_length=100, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='father_occupation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Father Occupation'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='guardian_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Guardian Name'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='mother_occupation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Mother Occupation'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='state',
            field=models.CharField(default='Tamil Nadu', max_length=100, verbose_name='State'),
        ),
    ]
