# Generated by Django 5.1.6 on 2025-02-26 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivw', '0012_alter_demand_status_actionplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionplan',
            name='status',
            field=models.CharField(default='Pendente', max_length=50),
        ),
    ]
