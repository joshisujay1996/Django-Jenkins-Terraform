# Generated by Django 2.2.4 on 2019-08-23 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20190823_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
        migrations.RemoveField(
            model_name='job',
            name='time',
        ),
    ]