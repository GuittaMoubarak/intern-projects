# Generated by Django 4.2.1 on 2023-05-31 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0003_alter_task_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='addDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
