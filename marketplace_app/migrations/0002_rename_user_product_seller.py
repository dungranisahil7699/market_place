# Generated by Django 5.0.3 on 2024-03-11 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user',
            new_name='seller',
        ),
    ]
