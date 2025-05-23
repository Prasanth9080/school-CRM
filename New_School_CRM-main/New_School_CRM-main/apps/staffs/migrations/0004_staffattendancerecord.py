# Generated by Django 5.1.5 on 2025-04-25 12:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0003_leaverequeststaff'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffAttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('month', models.CharField(max_length=20)),
                ('day', models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday')], max_length=10)),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('permission', 'Permission')], max_length=15)),
                ('message', models.TextField(blank=True)),
                ('signature', models.CharField(blank=True, max_length=100)),
                ('staff', models.ForeignKey(limit_choices_to={'groups__name': 'STAFF'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
