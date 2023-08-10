# Generated by Django 4.2.4 on 2023-08-09 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=254, null=True)),
                ('city', models.CharField(blank=True, max_length=254, null=True)),
                ('state', models.CharField(blank=True, max_length=254, null=True)),
                ('country', models.CharField(blank=True, max_length=254, null=True)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('referral_code', models.CharField(blank=True, max_length=10, null=True, unique=True)),
            ],
        ),
    ]
