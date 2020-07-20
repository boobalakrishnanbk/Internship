# Generated by Django 2.2.6 on 2019-10-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0046_auto_20191025_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetail',
            name='Photo',
            field=models.FileField(blank=True, null=True, upload_to='user_image/', verbose_name='Staff Photo'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='adhar_number',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Adhar Number'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='blood_group',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Blood Group'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date Of Birth'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='date_of_joining',
            field=models.DateField(blank=True, null=True, verbose_name='Date Of Joining'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email Id'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('', 'Select'), ('single', 'Single'), ('married', 'Married')], max_length=15, null=True, verbose_name='Marital Status'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='permanent_address',
            field=models.TextField(blank=True, null=True, verbose_name='Permanent Address'),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='present_address',
            field=models.TextField(blank=True, null=True, verbose_name='Present Address'),
        ),
    ]
