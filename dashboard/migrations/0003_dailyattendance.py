# Generated by Django 3.1.2 on 2020-10-14 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(choices=[('is_present', 'present'), ('is_absent', 'absent')], default='absent', max_length=20)),
                ('punch_time', models.DateTimeField()),
                ('punch_out_time', models.DateTimeField()),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.employee')),
            ],
        ),
    ]