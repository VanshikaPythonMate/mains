# Generated by Django 2.1.8 on 2021-03-20 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('door', '0003_siteglance_thingname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteglance',
            old_name='what',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='siteglance',
            old_name='thingname',
            new_name='thing_name',
        ),
    ]