# Generated by Django 4.2.2 on 2023-12-28 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0017_alter_trip_boarding_point_alter_trip_dropping_point_and_more'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('authentication', '0009_rename_full_name_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='User',
        ),
    ]