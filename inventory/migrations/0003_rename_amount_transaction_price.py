# Generated by Django 5.1.2 on 2025-02-08 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_axie_axie_class_remove_axie_cards_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='amount',
            new_name='price',
        ),
    ]
