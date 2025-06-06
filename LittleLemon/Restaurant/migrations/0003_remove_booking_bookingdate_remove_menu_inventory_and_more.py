# Generated by Django 5.2 on 2025-04-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_alter_menu_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='BookingDate',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='Inventory',
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_guest',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='bookingDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
    ]
