# Generated by Django 2.1.1 on 2018-10-09 15:26

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
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('notice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.IntegerField(default=0, unique=True)),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=44)),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=85)),
                ('tm', models.IntegerField(default=0)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='TestRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=0)),
                ('rks', models.CharField(max_length=44)),
                ('stu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student',
                                          to='sms.Student')),
                ('test',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='sms.Test')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='stu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Student'),
        ),
    ]
