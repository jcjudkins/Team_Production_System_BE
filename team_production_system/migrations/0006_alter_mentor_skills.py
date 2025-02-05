# Generated by Django 4.2.1 on 2023-05-24 21:46

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('team_production_system', '0005_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AWS S3', 'AWS S3'), ('Bootstrap', 'Bootstrap'), ('CSS', 'CSS'), ('Django', 'Django'), ('Git', 'Git'), ('GitHub', 'GitHub'), ('HTML', 'HTML'), ('Insomnia', 'Insomnia'), ('JavaScript', 'JavaScript'), ('MUI', 'MUI'), ('Other', 'Other'), ('PostgreSQL', 'PostgreSQL'), ('Postico', 'Postico'), ('Python', 'Python'), ('React', 'React'), ('SQL', 'SQL'), ('Time Management', 'Time Management')], default='HTML', max_length=52),
        ),
    ]
