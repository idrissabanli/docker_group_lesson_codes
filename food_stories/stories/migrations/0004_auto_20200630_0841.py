# Generated by Django 3.0.7 on 2020-06-30 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20200630_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('category', models.CharField(choices=[('cg', 'Convenience Goods'), ('shg', 'Shopping Goods'), ('sg', 'Specialty Goods')], max_length=5)),
                ('picture', models.ImageField(upload_to='media/products/images/')),
                ('amount', models.PositiveSmallIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('production_date', models.DateTimeField(auto_now_add=True)),
                ('is_new', models.BooleanField(default=False)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='media/products/files/')),
                ('rating', models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2, null=True)),
                ('detailed_view_link', models.URLField(max_length=300, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('-created_at', '-title'), 'verbose_name': 'Resept', 'verbose_name_plural': 'Reseptler'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='short_description',
            field=models.CharField(help_text='Bu sahe repestler siyahisinda reseptin mezmunu olaraq gorunur...', max_length=255, verbose_name='Qisa Mezmunu'),
        ),
    ]
