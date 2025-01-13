# Generated by Django 5.1.3 on 2025-01-13 17:59

import django.db.models.deletion
import django.db.models.manager
import timescale.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('ticker', models.CharField(db_index=True, max_length=20, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('close_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('high_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('low_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('number_of_trades', models.BigIntegerField(blank=True, null=True)),
                ('volume', models.BigIntegerField()),
                ('volume_weighted_average', models.DecimalField(decimal_places=4, max_digits=10)),
                ('time', timescale.db.models.fields.TimescaleDateTimeField(interval='1 week')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_quotes', to='market.company')),
            ],
            managers=[
                ('timescale', django.db.models.manager.Manager()),
            ],
        ),
    ]
