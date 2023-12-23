# Generated by Django 4.1.4 on 2023-07-18 14:46

import carousel.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=carousel.models.CarouselImage.image_upload_to)),
            ],
        ),
    ]
