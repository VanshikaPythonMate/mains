# Generated by Django 3.1.7 on 2021-04-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0013_user_can_create_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
