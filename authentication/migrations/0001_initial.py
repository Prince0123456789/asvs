# Generated by Django 4.1.4 on 2023-06-22 09:23

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(db_index=True, max_length=255)),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='password')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('approved', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=authentication.models.User.get_upload_path)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('signup_from', models.CharField(choices=[('web', 'web'), ('app', 'app')], default='web', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
