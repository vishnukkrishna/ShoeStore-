# Generated by Django 4.1.7 on 2023-03-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_carousel_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, upload_to='brands'),
        ),
    ]