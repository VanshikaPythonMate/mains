# Generated by Django 3.1.7 on 2021-12-16 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20210523_1904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentsubscriptionrecord',
            options={'ordering': ('-expiry_date',)},
        ),
    ]
