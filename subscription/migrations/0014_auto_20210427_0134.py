# Generated by Django 3.1.7 on 2021-04-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0013_auto_20210427_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionquestioncategory',
            name='evaluation_cost',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='subscriptionquestioncategory',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]