# Generated by Django 2.1.8 on 2021-03-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammanagerrelation',
            name='can_create_subscription',
            field=models.BooleanField(default=True),
        ),
    ]
