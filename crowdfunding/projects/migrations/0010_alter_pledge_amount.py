# Generated by Django 4.2.3 on 2023-09-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_goal_alter_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='amount',
            field=models.FloatField(),
        ),
    ]
