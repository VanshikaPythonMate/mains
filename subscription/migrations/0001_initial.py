# Generated by Django 2.1.8 on 2021-03-08 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSubscriptionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=30, unique=True)),
                ('full_name', models.CharField(max_length=150, null=True)),
                ('paid', models.BigIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subscription_of_student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'StudentSubscriptionRecord',
                'verbose_name_plural': 'StudentSubscriptionsRecord',
            },
        ),
        migrations.CreateModel(
            name='StudentSubscriptionsQuestionsNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('question_number', models.IntegerField()),
                ('student_subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentSubscription_questions_record', to='subscription.StudentSubscriptionRecord')),
            ],
            options={
                'verbose_name': 'StudentSubscriptionsQuestionsNumbers',
                'verbose_name_plural': 'StudentSubscriptionsQuestionsNumberss',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('days', models.CharField(max_length=30)),
                ('price', models.BigIntegerField()),
                ('active', models.BooleanField(default=True)),
                ('selling_points', models.TextField(null=True)),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
                ('expiry_date', models.DateField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subscription_created_by', to=settings.AUTH_USER_MODEL)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subscription_for_Exam', to='exam.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionQuestionAllowence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('question_number', models.IntegerField()),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Questions_allowence_to_Subscription', to='subscription.Subscription')),
            ],
        ),
    ]
