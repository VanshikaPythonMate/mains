# Generated by Django 3.1.7 on 2021-04-17 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0010_auto_20210410_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]