# Generated by Django 4.2.3 on 2023-08-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_image_alter_project_is_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
