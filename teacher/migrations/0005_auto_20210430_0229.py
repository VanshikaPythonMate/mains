# Generated by Django 3.1.7 on 2021-04-29 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20210429_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluatorglance',
            name='closed_details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='glanceevaluationsrecord',
            name='glance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='glance_evaluation', to='teacher.evaluatorglance'),
        ),
    ]
