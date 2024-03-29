# Generated by Django 3.0.7 on 2020-07-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='min_read_time',
            field=models.PositiveIntegerField(default=1, verbose_name='Min read time'),
        ),
        migrations.AddField(
            model_name='story',
            name='min_read_time',
            field=models.PositiveIntegerField(default=1, verbose_name='Min read time'),
        ),
    ]
