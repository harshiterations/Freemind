# Generated by Django 4.2.10 on 2024-08-18 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('availability', '0003_slot_therapist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='therapist',
        ),
    ]
