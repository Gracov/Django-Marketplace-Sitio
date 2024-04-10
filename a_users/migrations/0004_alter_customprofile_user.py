# Generated by Django 4.2.6 on 2024-04-10 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('a_users', '0003_alter_customprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customprofile',
            name='user',
            field=models.OneToOneField(default=9, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
