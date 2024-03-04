# Generated by Django 4.2.2 on 2024-03-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0003_alter_userdetails_options_userdetails_diabetic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
