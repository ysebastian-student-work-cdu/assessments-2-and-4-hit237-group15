# Generated by Django 4.2 on 2023-05-29 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_ingredients_user_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audit_record',
            old_name='category',
            new_name='audit_date',
        ),
        migrations.RenameField(
            model_name='audit_record',
            old_name='expiryDate',
            new_name='food_item',
        ),
        migrations.RenameField(
            model_name='audit_record',
            old_name='name',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='audit_record',
            old_name='itemID',
            new_name='waste_quantity',
        ),
    ]