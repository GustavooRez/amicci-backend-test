# Generated by Django 5.1.7 on 2025-03-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briefings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
