# Generated by Django 5.1.5 on 2025-04-23 12:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0009_userprofile_role'),
        ('students', '0004_alter_leaverequeststudent_date_applied'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StuReportCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamil', models.PositiveIntegerField()),
                ('english', models.PositiveIntegerField()),
                ('maths', models.PositiveIntegerField()),
                ('science', models.PositiveIntegerField()),
                ('social', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('pass', 'Pass'), ('fail', 'Fail')], max_length=10)),
                ('comments', models.TextField(blank=True)),
                ('parent_signature', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('standard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.studentclass')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
