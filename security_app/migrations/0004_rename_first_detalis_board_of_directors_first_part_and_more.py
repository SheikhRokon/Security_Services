# Generated by Django 4.1.6 on 2023-02-15 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security_app', '0003_board_of_directors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board_of_directors',
            old_name='first_detalis',
            new_name='first_part',
        ),
        migrations.RenameField(
            model_name='board_of_directors',
            old_name='last_detalis',
            new_name='secend_part',
        ),
    ]
