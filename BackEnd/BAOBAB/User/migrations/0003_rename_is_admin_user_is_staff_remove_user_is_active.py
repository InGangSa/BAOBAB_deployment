# Generated by Django 4.1 on 2023-07-29 14:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0002_alter_userimage_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_admin",
            new_name="is_staff",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
    ]
