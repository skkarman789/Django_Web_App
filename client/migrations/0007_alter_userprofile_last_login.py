# Generated by Django 5.0.3 on 2024-03-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_userprofile_date_joined_alter_usertask_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]