# Generated by Django 2.2 on 2019-04-29 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_list',
            new_name='tasklist',
        ),
    ]
