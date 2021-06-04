# Generated by Django 3.2.2 on 2021-06-03 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intcoal', '0004_rename_task_tasks_task_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='habits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='thoughts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thought_name', models.CharField(max_length=1000)),
            ],
        ),
    ]