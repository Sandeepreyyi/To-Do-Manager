# Generated by Django 5.1.3 on 2024-11-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blood_group_type',
            field=models.CharField(choices=[('o+', 'O+'), ('a+', 'A+'), ('b+', 'B+'), ('ab+', 'AB+'), ('o-', 'O-'), ('a-', 'A-'), ('b-', 'B-'), ('ab-', 'AB-')], default='o+', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
