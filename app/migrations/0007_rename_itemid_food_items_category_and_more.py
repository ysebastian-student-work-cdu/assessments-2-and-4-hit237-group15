# Generated by Django 4.2 on 2023-05-29 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_category_audit_record_audit_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food_items',
            old_name='itemID',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='food_items',
            old_name='wasteID',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='food_items',
            old_name='quantityWasted',
            new_name='quantity',
        ),
    ]
