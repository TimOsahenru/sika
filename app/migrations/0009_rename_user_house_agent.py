# Generated by Django 4.0.3 on 2022-08-09 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='user',
            new_name='agent',
        ),
    ]
