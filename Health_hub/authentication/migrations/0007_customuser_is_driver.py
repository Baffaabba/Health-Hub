# Generated by Django 4.2.2 on 2023-10-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_remove_customuser_details_userdetails_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_driver',
            field=models.BooleanField(default=False),
        ),
    ]
