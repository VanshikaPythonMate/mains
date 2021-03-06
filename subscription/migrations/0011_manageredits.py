# Generated by Django 2.1.8 on 2021-04-17 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0010_auto_20210410_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerEdits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(default='Create', max_length=30)),
                ('note', models.TextField(null=True)),
                ('content', models.TextField()),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_creating_manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
