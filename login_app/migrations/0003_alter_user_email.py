# Generated by Django 5.0.7 on 2024-07-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_remove_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=225),
        ),
    ]
