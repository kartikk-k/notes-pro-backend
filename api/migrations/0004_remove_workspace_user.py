# Generated by Django 4.1.5 on 2023-01-03 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_workspace_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspace',
            name='user',
        ),
    ]
