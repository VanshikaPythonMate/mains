# Generated by Django 3.1.7 on 2021-05-15 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0017_delete_subscriptionextras'),
        ('evaluation', '0010_auto_20210515_0640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evaluation',
            options={'ordering': ('-date_time_recent',)},
        ),
        migrations.AddField(
            model_name='evaluation',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscribed_subscription_que_category', to='subscription.subscriptionquestioncategory'),
        ),
    ]