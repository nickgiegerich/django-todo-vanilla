# Generated by Django 3.0.4 on 2020-03-23 05:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200323_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='line',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
