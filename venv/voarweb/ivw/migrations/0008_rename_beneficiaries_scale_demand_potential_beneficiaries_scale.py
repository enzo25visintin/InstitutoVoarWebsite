# Generated by Django 5.1.6 on 2025-02-21 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ivw', '0007_demand_beneficiaries_scale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demand',
            old_name='beneficiaries_scale',
            new_name='potential_beneficiaries_scale',
        ),
    ]
