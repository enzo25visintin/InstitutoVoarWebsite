# Generated by Django 5.1.6 on 2025-02-21 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivw', '0006_demand'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='beneficiaries_scale',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demand',
            name='potential_beneficiaries',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demand',
            name='potential_effort_scale',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demand',
            name='potential_impact_scale',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demand',
            name='status',
            field=models.CharField(default='Aguardando Priorização', max_length=50),
        ),
        migrations.CreateModel(
            name='Demands_x_Materiality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ivw.demand')),
                ('materiality_issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ivw.materiality_issue')),
            ],
        ),
        migrations.CreateModel(
            name='SDG_x_Demands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ivw.demand')),
                ('sdg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ivw.sdg')),
            ],
        ),
        migrations.CreateModel(
            name='Stakeholder_x_Demands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ivw.demand')),
                ('stakeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ivw.stakeholder')),
            ],
        ),
    ]
