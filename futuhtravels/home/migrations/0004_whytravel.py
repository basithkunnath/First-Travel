# Generated by Django 5.1.3 on 2024-11-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_introduction_welcome_paragraph'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whytravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whytravel_title', models.CharField(max_length=100)),
                ('feature_one', models.CharField(max_length=300)),
                ('feature_two', models.CharField(max_length=300)),
                ('feature_three', models.CharField(max_length=300)),
                ('feature_four', models.CharField(max_length=300)),
            ],
        ),
    ]
