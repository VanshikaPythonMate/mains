# Generated by Django 3.1.7 on 2021-04-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0012_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='can_create_subscription',
            field=models.BooleanField(default=False),
        ),
    ]
