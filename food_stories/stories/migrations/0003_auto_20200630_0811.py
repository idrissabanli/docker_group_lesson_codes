# Generated by Django 3.0.7 on 2020-06-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20200630_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='image.png', upload_to='media/recipes', verbose_name='Sekil'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='long_description',
            field=models.TextField(default='long desc', verbose_name='Genis mezmunu'),
            preserve_default=False,
        ),
    ]