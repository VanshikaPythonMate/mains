# Generated by Django 2.1.8 on 2021-03-09 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0004_auto_20210308_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isVarified',
            field=models.BooleanField(default=True),
        ),
    ]
