# Generated by Django 2.1.8 on 2021-03-08 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentSubscriptionsQuestionsNumbers',
            new_name='StudentSubscriptionsQuestionsRecord',
        ),
        migrations.AlterModelOptions(
            name='studentsubscriptionrecord',
            options={'verbose_name': 'StudentSubscriptionRecord', 'verbose_name_plural': 'StudentSubscriptionRecord'},
        ),
        migrations.AlterModelOptions(
            name='studentsubscriptionsquestionsrecord',
            options={'verbose_name': 'StudentSubscriptionsQuestionsRecord', 'verbose_name_plural': 'StudentSubscriptionsQuestionsRecord'},
        ),
        migrations.RenameField(
            model_name='studentsubscriptionrecord',
            old_name='full_name',
            new_name='exam_full_name',
        ),
        migrations.RenameField(
            model_name='studentsubscriptionrecord',
            old_name='short_name',
            new_name='exam_short_name',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='expiry_date',
            new_name='limited_time_to',
        ),
        migrations.AddField(
            model_name='studentsubscriptionrecord',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='description',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]
