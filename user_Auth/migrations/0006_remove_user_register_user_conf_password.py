# Generated by Django 4.1.3 on 2023-02-08 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_Auth', '0005_user_register_delete_user_resgisteration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_register',
            name='user_conf_password',
        ),
    ]