# Generated by Django 4.2.6 on 2023-10-05 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='requested_by',
        ),
    ]
