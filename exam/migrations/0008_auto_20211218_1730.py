# Generated by Django 3.1.7 on 2021-12-18 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20210521_2333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ('-id', 'short_name')},
        ),
    ]
