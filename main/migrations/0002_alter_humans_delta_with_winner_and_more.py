# Generated by Django 5.1.3 on 2024-12-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humans',
            name='delta_with_winner',
            field=models.TimeField(verbose_name='delta_with_winner'),
        ),
        migrations.AlterField(
            model_name='humans',
            name='result_time',
            field=models.TimeField(verbose_name='result_time'),
        ),
        migrations.AlterField(
            model_name='humans',
            name='winner_time',
            field=models.TimeField(verbose_name='winner_time'),
        ),
    ]
