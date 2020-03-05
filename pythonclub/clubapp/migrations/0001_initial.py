# Generated by Django 3.0.2 on 2020-03-04 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingtitle', models.CharField(max_length=255)),
                ('meetingdate', models.DateField()),
                ('meetingtime', models.TimeField()),
                ('meetinglocation', models.CharField(max_length=255)),
                ('meetingagenda', models.TextField()),
            ],
            options={
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResourceName', models.CharField(max_length=255)),
                ('resourcetype', models.CharField(max_length=255)),
                ('resourceurl', models.URLField()),
                ('resourcedateentered', models.DateField()),
                ('resourceid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clubapp.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MeetingMinutesTitle', models.CharField(max_length=255)),
                ('meetingattendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meetingid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clubapp.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventTitle', models.CharField(max_length=255)),
                ('eventlocation', models.CharField(max_length=255)),
                ('eventdate', models.DateField()),
                ('eventtime', models.TimeField()),
                ('eventdescription', models.TextField()),
                ('eventuserid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
