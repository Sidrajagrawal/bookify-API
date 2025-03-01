# Generated by Django 5.1.5 on 2025-01-26 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sell_detail', '0003_selldetail_sale_count_selldetail_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sell_detail.selldetail')),
            ],
        ),
    ]
