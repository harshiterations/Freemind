# Generated by Django 4.2.10 on 2024-08-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0004_alter_therapist_slot_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapist',
            name='slot_duration',
            field=models.IntegerField(default=30),
        ),
    ]
