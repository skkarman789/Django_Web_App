# Generated by Django 5.0.3 on 2024-03-06 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_usertasks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserTasks',
            new_name='UserTask',
        ),
    ]