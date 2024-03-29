# Generated by Django 4.1.4 on 2023-07-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asvs_app', '0002_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
