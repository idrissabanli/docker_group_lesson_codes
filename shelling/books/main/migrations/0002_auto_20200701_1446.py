# Generated by Django 3.0.8 on 2020-07-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='books', to='main.Category', verbose_name='Categories'),
        ),
    ]
