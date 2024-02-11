# Generated by Django 5.0.1 on 2024-02-07 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0030_customuser_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]