# Generated by Django 5.1.3 on 2024-11-11 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_whytravel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingTrips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upcoming_title', models.CharField(max_length=100)),
                ('package_image', models.ImageField(blank=True, null=True, upload_to='package_images/')),
                ('package_title', models.CharField(max_length=100)),
                ('package_shot_description', models.CharField(max_length=100)),
            ],
        ),
    ]
