# Generated by Django 3.2.11 on 2022-02-15 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routemonitor', '0002_auto_20220215_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='project',
        ),
        migrations.AddField(
            model_name='schedule',
            name='route',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='routemonitor.route'),
            preserve_default=False,
        ),
    ]