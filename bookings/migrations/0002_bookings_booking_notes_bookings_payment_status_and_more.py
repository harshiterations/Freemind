# Generated by Django 4.2.10 on 2024-08-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='booking_notes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='payment_status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('canceled', 'Canceled')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='status',
            field=models.CharField(choices=[('UPCOMING', 'Upcoming'), ('ACTIVE', 'Active'), ('PAST', 'Past')], max_length=70, null=True),
        ),
    ]
