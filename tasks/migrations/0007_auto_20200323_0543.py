# Generated by Django 3.0.4 on 2020-03-23 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_line'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskline',
            options={},
        ),
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.RemoveField(
            model_name='task',
            name='descr',
        ),
        migrations.RemoveField(
            model_name='task',
            name='line',
        ),
    ]
