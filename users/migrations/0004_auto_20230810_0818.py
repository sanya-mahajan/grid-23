# Generated by Django 3.2.18 on 2023-08-10 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230810_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degree',
            name='user',
        ),
        migrations.RemoveField(
            model_name='therapist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='mhp_is_verified',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='parent_otp',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='parental_consent',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'CUSTOMER'), (2, 'ADMIN')], default=1),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Degree',
        ),
        migrations.DeleteModel(
            name='Therapist',
        ),
    ]
