# Generated by Django 5.1.5 on 2025-01-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell_detail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='selldetail',
            name='book_AI_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='selldetail',
            name='book_edition',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='selldetail',
            name='book_isbn',
            field=models.CharField(max_length=13, null=True, unique=True),
        ),
    ]
