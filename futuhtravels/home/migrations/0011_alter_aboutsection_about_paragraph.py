# Generated by Django 5.1.3 on 2024-11-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_aboutsection_about_paragraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutsection',
            name='about_paragraph',
            field=models.CharField(max_length=1200),
        ),
    ]
