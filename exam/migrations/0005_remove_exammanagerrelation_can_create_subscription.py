# Generated by Django 3.1.7 on 2021-04-24 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20210405_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exammanagerrelation',
            name='can_create_subscription',
        ),
    ]
