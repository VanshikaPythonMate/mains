# Generated by Django 2.1.8 on 2021-04-04 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0003_auto_20210328_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evaluation',
            options={'ordering': ('-date_time_recent',)},
        ),
    ]