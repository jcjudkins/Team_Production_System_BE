# Generated by Django 4.2.1 on 2023-06-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_production_system', '0008_alter_mentor_skills'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='availability',
            constraint=models.UniqueConstraint(fields=('mentor', 'start_time'), name='availability_constraint'),
        ),
    ]
