# Generated by Django 4.2.6 on 2023-10-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_appointment_notes_appointment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='title',
            field=models.CharField(max_length=40, null=True),
        ),
    ]