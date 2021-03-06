# Generated by Django 3.0.7 on 2020-07-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20200721_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='min_read_time',
            field=models.PositiveIntegerField(default=1, editable=False, verbose_name='Min read time'),
        ),
        migrations.AlterField(
            model_name='story',
            name='min_read_time',
            field=models.PositiveIntegerField(default=1, editable=False, verbose_name='Min read time'),
        ),
    ]
