# Generated by Django 4.0.3 on 2022-09-17 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_house_image_houseimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.houseimage'),
        ),
    ]
