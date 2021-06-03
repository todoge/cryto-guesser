# Generated by Django 3.2.4 on 2021-06-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guess',
            name='coin',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='guess',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
    ]