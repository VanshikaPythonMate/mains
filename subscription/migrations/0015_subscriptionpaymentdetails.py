# Generated by Django 3.1.7 on 2021-05-01 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0014_auto_20210427_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.TextField(null=True)),
                ('order_obj', models.TextField(null=True)),
                ('receipt_id', models.TextField(null=True)),
                ('payment_id', models.TextField(null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('last_saved', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_student', to=settings.AUTH_USER_MODEL)),
                ('subscription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscription_payment_details', to='subscription.subscription')),
            ],
            options={
                'ordering': ('-last_saved',),
            },
        ),
    ]
