# Generated by Django 4.2.3 on 2023-08-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
