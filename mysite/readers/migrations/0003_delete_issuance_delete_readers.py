# Generated by Django 4.2.1 on 2023-06-04 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0002_issuance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Issuance',
        ),
        migrations.DeleteModel(
            name='Readers',
        ),
    ]
