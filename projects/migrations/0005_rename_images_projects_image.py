# Generated by Django 5.1.1 on 2024-10-02 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projects_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='images',
            new_name='image',
        ),
    ]
