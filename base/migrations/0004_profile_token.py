# Generated by Django 4.2.8 on 2024-03-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_profile_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
