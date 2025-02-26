# Generated by Django 5.1.4 on 2025-01-06 05:26

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RubberType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bag_weight', models.DecimalField(decimal_places=2, help_text='Weight per bag in kg', max_digits=5)),
                ('price_per_kg', models.DecimalField(decimal_places=2, help_text='Selling price per kg', max_digits=7)),
                ('stock_bags', models.PositiveIntegerField(default=0, help_text='Number of bags in stock')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(default=datetime.date.today)),
                ('arrival_date', models.DateField(blank=True, help_text='Date goods arrive at warehouse', null=True)),
                ('bags_received', models.PositiveIntegerField(default=0, help_text='Number of bags received')),
                ('customs_cost', models.DecimalField(decimal_places=2, help_text='Customs and import charges', max_digits=10)),
                ('transport_cost', models.DecimalField(decimal_places=2, help_text='Logistics cost', max_digits=10)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, help_text='Total cost of shipment', max_digits=10, null=True)),
                ('cost_per_kg', models.DecimalField(blank=True, decimal_places=2, help_text='Calculated cost per kg', max_digits=7, null=True)),
                ('rubber_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.rubbertype')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateField(default=datetime.date.today)),
                ('bags_sold', models.PositiveIntegerField(default=0)),
                ('selling_price_per_kg', models.DecimalField(decimal_places=2, help_text='Selling price per kg', max_digits=7)),
                ('revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rubber_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.rubbertype')),
            ],
        ),
    ]
