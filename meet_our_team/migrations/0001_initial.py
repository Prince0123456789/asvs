# Generated by Django 4.1.4 on 2023-07-19 15:26

from django.db import migrations, models
import meet_our_team.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=meet_our_team.models.Team.upload_team_image)),
                ('is_active', models.BooleanField(default=True)),
                ('facebook_link', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('twiiter_link', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
    ]
