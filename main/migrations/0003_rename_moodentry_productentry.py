# Generated by Django 5.1.1 on 2024-09-17 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_moodentry_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MoodEntry',
            new_name='ProductEntry',
        ),
    ]
