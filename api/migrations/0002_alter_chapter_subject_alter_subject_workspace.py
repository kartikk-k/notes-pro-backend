# Generated by Django 4.1.4 on 2022-12-19 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.workspace'),
        ),
    ]