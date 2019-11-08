# Generated by Django 2.2.6 on 2019-11-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('department', models.CharField(max_length=5)),
                ('student_name', models.CharField(max_length=100)),
                ('cpi', models.FloatField()),
                ('skills', models.TextField(max_length=100)),
            ],
        ),
    ]
