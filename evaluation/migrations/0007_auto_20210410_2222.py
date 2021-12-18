# Generated by Django 2.1.8 on 2021-04-10 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0006_auto_20210406_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='evaluator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='selected_evaluator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='for_exam', to='exam.Exam'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscribed_subscription', to='student.StudentSubscriptionsQuestionsRecord'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='subscribed_subscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscribed_subscription', to='student.StudentSubscriptionRecord'),
        ),
    ]
