# Generated by Django 3.0.4 on 2020-03-20 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='descr',
            field=models.CharField(default='Before Description', max_length=750),
        ),
    ]