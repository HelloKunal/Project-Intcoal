# Generated by Django 3.2.2 on 2021-06-03 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intcoal', '0003_auto_20210603_0712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='task',
            new_name='task_name',
        ),
    ]