# Generated by Django 4.0.3 on 2022-09-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_house_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='image',
            new_name='image_one',
        ),
        migrations.AddField(
            model_name='house',
            name='image_three',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='house',
            name='image_two',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]