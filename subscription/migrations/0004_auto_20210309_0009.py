# Generated by Django 2.1.8 on 2021-03-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0003_auto_20210308_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='days',
            field=models.IntegerField(),
        ),
    ]
