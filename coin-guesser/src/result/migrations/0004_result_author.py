# Generated by Django 3.2.4 on 2021-06-05 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('result', '0003_remove_result_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='author',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='result', to='auth.user'),
            preserve_default=False,
        ),
    ]